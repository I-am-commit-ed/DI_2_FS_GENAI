import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "restaurant",
    "user": "postgres",
    "password": "YOUR_PASSWORD",
    "host": "localhost",
    "port": 5432,
}

def get_connection():
    """
    Returns a new connection. Use with 'with get_connection() as conn:'.
    """
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
