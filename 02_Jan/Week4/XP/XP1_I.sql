-- 1) Create database (run from a postgres/admin connection)
CREATE DATABASE restaurant;

-- 2) Connect to restaurant DB, then:
CREATE TABLE IF NOT EXISTS menu_items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL UNIQUE,
    item_price SMALLINT DEFAULT 0 CHECK (item_price >= 0)
);