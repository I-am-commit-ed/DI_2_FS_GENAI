/* ============================================================
   TABLE RELATIONSHIPS PRACTICE (PostgreSQL)
   Part I: One-to-One (Customer <-> Customer_profile)
   Part II: Many-to-Many (Book <-> Student via Library)
   Copy/paste and run in order.
   ============================================================ */


/* =========================
   PART I — ONE TO ONE
   ========================= */

-- Clean up (so you can re-run)
DROP TABLE IF EXISTS customer_profile;
DROP TABLE IF EXISTS customer;

-- 1) Create tables
CREATE TABLE customer (
  id         SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name  VARCHAR(50) NOT NULL
);

CREATE TABLE customer_profile (
  id          SERIAL PRIMARY KEY,
  isLoggedIn  BOOLEAN NOT NULL DEFAULT FALSE,
  customer_id INTEGER NOT NULL UNIQUE REFERENCES customer(id)
);

-- 2) Insert customers
INSERT INTO customer (first_name, last_name) VALUES
  ('John',   'Doe'),
  ('Jerome', 'Lalu'),
  ('Lea',    'Rive');

-- 3) Insert profiles (use subqueries)
-- John is logged in
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES (
  TRUE,
  (SELECT id FROM customer WHERE first_name = 'John' AND last_name = 'Doe')
);

-- Jerome is not logged in
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES (
  FALSE,
  (SELECT id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu')
);

-- 4a) The first_name of the LoggedIn customers
-- Use INNER JOIN (only those with profiles), and filter isLoggedIn = true
SELECT c.first_name
FROM customer c
JOIN customer_profile cp
  ON cp.customer_id = c.id
WHERE cp.isLoggedIn = TRUE;

-- 4b) All customers first_name and isLoggedIn, even those without a profile
-- Use LEFT JOIN (keep all customers)
SELECT
  c.first_name,
  cp.isLoggedIn
FROM customer c
LEFT JOIN customer_profile cp
  ON cp.customer_id = c.id
ORDER BY c.first_name;

-- 4c) Number of customers that are NOT LoggedIn
-- Customers with no profile should count as NOT logged in (treat NULL as false)
SELECT COUNT(*) AS not_logged_in_count
FROM customer c
LEFT JOIN customer_profile cp
  ON cp.customer_id = c.id
WHERE COALESCE(cp.isLoggedIn, FALSE) = FALSE;


/* =========================
   PART II — MANY TO MANY
   Book <-> Student via Library (junction table)
   ========================= */

-- Clean up
DROP TABLE IF EXISTS library;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS book;

-- 1) Create Book table
CREATE TABLE book (
  book_id SERIAL PRIMARY KEY,
  title   VARCHAR(255) NOT NULL,
  author  VARCHAR(255) NOT NULL
);

-- Insert books
INSERT INTO book (title, author) VALUES
  ('Alice In Wonderland', 'Lewis Carroll'),
  ('Harry Potter', 'J.K Rowling'),
  ('To kill a mockingbird', 'Harper Lee');

-- 2) Create Student table (age never bigger than 15)
-- Use a CHECK constraint
CREATE TABLE student (
  student_id SERIAL PRIMARY KEY,
  name       VARCHAR(100) NOT NULL UNIQUE,
  age        INTEGER CHECK (age <= 15)
);

-- Insert students
INSERT INTO student (name, age) VALUES
  ('John',    12),
  ('Lera',    11),
  ('Patrick', 10),
  ('Bob',     14);

-- 3) Create Library junction table
-- Pair of FKs is the PRIMARY KEY
CREATE TABLE library (
  book_fk_id     INTEGER NOT NULL,
  student_fk_id  INTEGER NOT NULL,
  borrowed_date  DATE NOT NULL,

  PRIMARY KEY (book_fk_id, student_fk_id),

  CONSTRAINT fk_library_book
    FOREIGN KEY (book_fk_id)
    REFERENCES book(book_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_library_student
    FOREIGN KEY (student_fk_id)
    REFERENCES student(student_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- 4) Add 4 records using subqueries
-- John borrowed Alice In Wonderland on 15/02/2022
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
  (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
  (SELECT student_id FROM student WHERE name = 'John'),
  TO_DATE('15/02/2022', 'DD/MM/YYYY')
);

-- Bob borrowed To kill a mockingbird on 03/03/2021
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
  (SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
  (SELECT student_id FROM student WHERE name = 'Bob'),
  TO_DATE('03/03/2021', 'DD/MM/YYYY')
);

-- Lera borrowed Alice In Wonderland on 23/05/2021
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
  (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
  (SELECT student_id FROM student WHERE name = 'Lera'),
  TO_DATE('23/05/2021', 'DD/MM/YYYY')
);

-- Bob borrowed Harry Potter on 12/08/2021
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
  (SELECT book_id FROM book WHERE title = 'Harry Potter'),
  (SELECT student_id FROM student WHERE name = 'Bob'),
  TO_DATE('12/08/2021', 'DD/MM/YYYY')
);

-- 5a) Display: select all columns from the junction table
SELECT *
FROM library
ORDER BY borrowed_date;

-- 5b) Display: student name + borrowed book title
SELECT
  s.name AS student_name,
  b.title AS book_title,
  l.borrowed_date
FROM library l
JOIN student s ON s.student_id = l.student_fk_id
JOIN book b    ON b.book_id = l.book_fk_id
ORDER BY s.name, b.title;

-- 5c) Average age of children who borrowed "Alice In Wonderland"
SELECT AVG(s.age) AS avg_age
FROM library l
JOIN student s ON s.student_id = l.student_fk_id
JOIN book b    ON b.book_id = l.book_fk_id
WHERE b.title = 'Alice In Wonderland';

-- 6) Delete a student from Student table, what happens in Library?
-- Because of ON DELETE CASCADE, their rows in library are deleted automatically.
-- Example: delete Patrick (he has no library rows, but this shows the idea)
DELETE FROM student
WHERE name = 'Patrick';

-- Check current library rows after deletion
SELECT *
FROM library
ORDER BY borrowed_date;
