-- (Optional) clean start
DROP TABLE IF EXISTS customer_profile;
DROP TABLE IF EXISTS customer;

CREATE TABLE customer (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name  VARCHAR(50) NOT NULL
);

CREATE TABLE customer_profile (
  id SERIAL PRIMARY KEY,
  isLoggedIn BOOLEAN NOT NULL DEFAULT FALSE,
  customer_id INT UNIQUE REFERENCES customer(id)  -- UNIQUE enforces 1-to-1
);


2) Insert customers
INSERT INTO customer (first_name, last_name)
VALUES
  ('John', 'Doe'),
  ('Jerome', 'Lalu'),
  ('Lea', 'Rive');

3) Insert profiles using subqueries
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES
  (TRUE,  (SELECT id FROM customer WHERE first_name='John'   AND last_name='Doe')),
  (FALSE, (SELECT id FROM customer WHERE first_name='Jerome' AND last_name='Lalu'));

4) Required queries (joins)
a) The first_name of the LoggedIn customers
SELECT c.first_name
FROM customer c
JOIN customer_profile cp
  ON cp.customer_id = c.id
WHERE cp.isLoggedIn = TRUE;

b) All customers first_name and isLoggedIn — even customers without a profile
SELECT c.first_name, cp.isLoggedIn
FROM customer c
LEFT JOIN customer_profile cp
  ON cp.customer_id = c.id;

c) Number of customers that are not LoggedIn

(Counts customers with isLoggedIn = false and customers with no profile as “not logged in”.)

SELECT COUNT(*) AS not_logged_in_count
FROM customer c
LEFT JOIN customer_profile cp
  ON cp.customer_id = c.id
WHERE COALESCE(cp.isLoggedIn, FALSE) = FALSE;

Part II — Many-to-Many: Student ↔ Book via Library
1) Create Book + insert books
DROP TABLE IF EXISTS library;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS book;

CREATE TABLE book (
  book_id SERIAL PRIMARY KEY,
  title  VARCHAR(200) NOT NULL,
  author VARCHAR(200) NOT NULL
);

INSERT INTO book (title, author)
VALUES
  ('Alice In Wonderland', 'Lewis Carroll'),
  ('Harry Potter', 'J.K Rowling'),
  ('To kill a mockingbird', 'Harper Lee');

2) Create Student with age constraint + insert students

Age constraint in SQL: CHECK (age <= 15)

CREATE TABLE student (
  student_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE,
  age INT CHECK (age <= 15)
);

INSERT INTO student (name, age)
VALUES
  ('John', 12),
  ('Lera', 11),
  ('Patrick', 10),
  ('Bob', 14);

3) Create junction table Library (Many-to-Many)
CREATE TABLE library (
  book_fk_id INT REFERENCES book(book_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  student_fk_id INT REFERENCES student(student_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  borrowed_date DATE NOT NULL,
  PRIMARY KEY (book_fk_id, student_fk_id)
);

4) Insert 4 records using subqueries
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES
  (
    (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM student WHERE name = 'John'),
    '2022-02-15'
  ),
  (
    (SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
    (SELECT student_id FROM student WHERE name = 'Bob'),
    '2021-03-03'
  ),
  (
    (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM student WHERE name = 'Lera'),
    '2021-05-23'
  ),
  (
    (SELECT book_id FROM book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM student WHERE name = 'Bob'),
    '2021-08-12'
  );

Display / Queries
a) Select all columns from the junction table
SELECT *
FROM library;

b) Select student name + title of borrowed books
SELECT s.name, b.title, l.borrowed_date
FROM library l
JOIN student s ON s.student_id = l.student_fk_id
JOIN book b    ON b.book_id    = l.book_fk_id
ORDER BY s.name, l.borrowed_date;

c) Average age of children who borrowed Alice In Wonderland
SELECT AVG(s.age) AS avg_age
FROM library l
JOIN student s ON s.student_id = l.student_fk_id
JOIN book b    ON b.book_id    = l.book_fk_id
WHERE b.title = 'Alice In Wonderland';

d) Delete a student — what happens in library?
DELETE FROM student
WHERE name = 'Bob';


What happens: because library.student_fk_id has ON DELETE CASCADE, all rows in library that referenced Bob are automatically deleted. You can verify:

SELECT *
FROM library;