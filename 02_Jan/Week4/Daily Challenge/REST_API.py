import os
import random
import requests
import psycopg2
from psycopg2.extras import execute_values

API_URL = "https://restcountries.com/v3.1/all"

# REST Countries returns:
# - name: object (use name.common)
# - capital: sometimes string or list
# - flags: object (often has png/svg)
# - subregion: string
# - population: integer
# :contentReference[oaicite:1]{index=1}

def get_db_connection():
    """
    Configure via env vars (recommended):
      DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
    """
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "your_db_name"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "your_password"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
    )

def ensure_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS countries (
              country_id  SERIAL PRIMARY KEY,
              name        TEXT UNIQUE NOT NULL,
              capital     TEXT,
              flag        TEXT,
              subregion   TEXT,
              population  BIGINT
            );
        """)
    conn.commit()

def normalize_capital(capital_value):
    if capital_value is None:
        return None
    if isinstance(capital_value, list):
        return capital_value[0] if capital_value else None
    return str(capital_value)

def normalize_flag(flags_obj):
    # Prefer PNG, fallback to SVG, else None
    if not isinstance(flags_obj, dict):
        return None
    return flags_obj.get("png") or flags_obj.get("svg")

def fetch_all_countries():
    # Using fields is important; /all can fail without it, and max is 10 fields.
    # :contentReference[oaicite:2]{index=2}
    params = {"fields": "name,capital,flags,subregion,population"}
    res = requests.get(API_URL, params=params, timeout=25)
    res.raise_for_status()
    return res.json()

def pick_random_countries(raw, n=10):
    cleaned = []
    for c in raw:
        name_obj = c.get("name") or {}
        name = name_obj.get("common") or name_obj.get("official")
        if not name:
            continue

        capital = normalize_capital(c.get("capital"))
        flag = normalize_flag(c.get("flags"))
        subregion = c.get("subregion")
        population = c.get("population", 0)

        # keep records even if some fields missing; but name is mandatory
        cleaned.append((name, capital, flag, subregion, population))

    if len(cleaned) == 0:
        raise RuntimeError("No valid country records found from API response.")

    n = min(n, len(cleaned))
    return random.sample(cleaned, n)

def insert_countries(conn, rows):
    """
    Upsert on country name to avoid duplicates if you run the script multiple times.
    """
    sql = """
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES %s
        ON CONFLICT (name) DO UPDATE SET
          capital    = EXCLUDED.capital,
          flag       = EXCLUDED.flag,
          subregion  = EXCLUDED.subregion,
          population = EXCLUDED.population;
    """
    with conn.cursor() as cur:
        execute_values(cur, sql, rows)
    conn.commit()

def main():
    raw = fetch_all_countries()
    rows = pick_random_countries(raw, n=10)

    conn = get_db_connection()
    try:
        ensure_table(conn)
        insert_countries(conn, rows)
        print("✅ Inserted 10 random countries into the database.")
        for r in rows:
            print(" -", r[0])
    finally:
        conn.close()

if __name__ == "__main__":
    main()
