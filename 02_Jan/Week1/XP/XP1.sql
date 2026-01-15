-- 🌟 Exercise 1: Items and customers
-- PostgreSQL version

-- Optional (often not allowed on Supabase / shared DBs):
-- CREATE DATABASE public;

-- Make sure we're using the public schema (default in Postgres)
SET search_path TO public;

-- Clean start (so you can re-run the file)
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS customers;

-- 1) Create tables
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  price INTEGER NOT NULL CHECK (price >= 0)
);

CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL
);

-- 2) Insert data
INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

INSERT INTO customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

-- 3) Queries

-- All the items.
SELECT * FROM items;

-- All the items with a price above 80 (80 not included).
SELECT * FROM items
WHERE price > 80;

-- All the items with a price below 300 (300 included).
SELECT * FROM items
WHERE price <= 300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
-- Outcome: empty result (0 rows), because we inserted no Smiths.
SELECT * FROM customers
WHERE last_name = 'Smith';

-- All customers whose last name is ‘Jones’.
SELECT * FROM customers
WHERE last_name = 'Jones';

-- All customers whose firstname is not ‘Scott’.
SELECT * FROM customers
WHERE first_name <> 'Scott';
