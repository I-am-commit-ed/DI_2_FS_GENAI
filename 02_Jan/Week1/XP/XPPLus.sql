-- Exercise: Students table (PostgreSQL)

-- OPTIONAL: only works if you have permission to create databases
-- CREATE DATABASE bootcamp;

-- Use public schema (default)
SET search_path TO public;

-- Clean start
DROP TABLE IF EXISTS students;

-- Create table
CREATE TABLE students (
  id SERIAL PRIMARY KEY,           -- auto-increment
  last_name  VARCHAR(50) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  birth_date DATE NOT NULL
);

-- Insert: efficient multi-row insert
INSERT INTO students (first_name, last_name, birth_date) VALUES
('Marc',   'Benichou', TO_DATE('02/11/1998', 'DD/MM/YYYY')),
('Yoan',   'Cohen',    TO_DATE('03/12/2010', 'DD/MM/YYYY')),
('Lea',    'Benichou', TO_DATE('27/07/1987', 'DD/MM/YYYY')),
('Amelia', 'Dux',      TO_DATE('07/04/1996', 'DD/MM/YYYY')),
('David',  'Grez',     TO_DATE('14/06/2003', 'DD/MM/YYYY')),
('Omer',   'Simpson',  TO_DATE('03/10/1980', 'DD/MM/YYYY'));

-- Insert YOUR row (replace with your real info)
-- Note: id is auto-generated, so you don't insert it.
INSERT INTO students (first_name, last_name, birth_date) VALUES
('Manuel', 'Kizer', TO_DATE('01/01/2000', 'DD/MM/YYYY'));

-- =========================================
-- SELECTS
-- =========================================

-- Fetch all data
SELECT * FROM students;

-- Fetch all students first_names and last_names
SELECT first_name, last_name FROM students;

-- For the following questions, only fetch first_names and last_names

-- Student with id = 2
SELECT first_name, last_name
FROM students
WHERE id = 2;

-- Student whose last_name is Benichou AND first_name is Marc
SELECT first_name, last_name
FROM students
WHERE last_name = 'Benichou'
  AND first_name = 'Marc';

-- Students whose last_names are Benichou OR first_names are Marc
SELECT first_name, last_name
FROM students
WHERE last_name = 'Benichou'
   OR first_name = 'Marc';

-- Students whose first_names contain the letter a (case-insensitive)
SELECT first_name, last_name
FROM students
WHERE first_name ILIKE '%a%';

-- Students whose first_names start with the letter a
SELECT first_name, last_name
FROM students
WHERE first_name ILIKE 'a%';

-- Students whose first_names end with the letter a
SELECT first_name, last_name
FROM students
WHERE first_name ILIKE '%a';

-- Students whose second to last letter of their first_names is 'a' (e.g., Leah)
-- pattern: _a% means: one char, then 'a', then anything after
SELECT first_name, last_name
FROM students
WHERE first_name ILIKE '%a_';

-- Students whose id’s are equal to 1 AND 3
SELECT first_name, last_name
FROM students
WHERE id IN (1, 3);

-- Students whose birth_dates are equal to or after 01/01/2000 (show all info)
SELECT *
FROM students
WHERE birth_date >= DATE '2000-01-01';


-- =========================================
-- CONTINUATION: SELECTS (first_name, last_name, birth_date)
-- =========================================

-- 1) Fetch the first four students, ordered alphabetically by last_name
SELECT first_name, last_name, birth_date
FROM students
ORDER BY last_name ASC
LIMIT 4;

-- 2) Fetch the details of the youngest student
-- Youngest = most recent birth_date
SELECT first_name, last_name, birth_date
FROM students
ORDER BY birth_date DESC
LIMIT 1;

-- 3) Fetch three students skipping the first two students
-- (Add an ORDER BY so "first two" is deterministic)
SELECT first_name, last_name, birth_date
FROM students
ORDER BY id ASC
LIMIT 3 OFFSET 2;
