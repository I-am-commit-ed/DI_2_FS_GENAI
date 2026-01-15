CREATE TABLE IF NOT EXISTS countries (
  country_id  SERIAL PRIMARY KEY,
  name        TEXT UNIQUE NOT NULL,
  capital     TEXT,
  flag        TEXT,
  subregion   TEXT,
  population  BIGINT
);
