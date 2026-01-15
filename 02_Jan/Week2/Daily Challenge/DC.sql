/* ============================================================
   ALL SQL ANSWERS IN ONE DOCUMENT (copy/paste)
   - Public DB: Exercise 1 (Items & Customers)
   - DVDRental DB: Exercise 2 (15 queries + optional bonus)
   - Public DB: Exercise 1 Bonus (Continuation)
   ============================================================ */


/* ============================================================
   PART A — PUBLIC DATABASE
   Exercise 1: Items and Customers
   Assumptions:
   - public.items(..., price, ...)
   - public.customers(id, first_name, last_name, ...)
   ============================================================ */

-- A1) All items, ordered by price (lowest to highest)
SELECT *
FROM public.items
ORDER BY price ASC;

-- A2) Items with a price >= 80, ordered by price (highest to lowest)
SELECT *
FROM public.items
WHERE price >= 80
ORDER BY price DESC;

-- A3) First 3 customers in alphabetical order of first_name (A-Z) – exclude primary key (id)
SELECT first_name, last_name
FROM public.customers
ORDER BY first_name ASC, last_name ASC
LIMIT 3;

-- A4) All last names only, reverse alphabetical order (Z-A)
SELECT last_name
FROM public.customers
ORDER BY last_name DESC;


/* ============================================================
   PART B — DVDrental DATABASE
   Exercise 2: dvdrental database
   Tables used: customer, film, address, payment, inventory, city, country
   ============================================================ */

-- B1) Select all columns from customer
SELECT *
FROM customer;

-- B2) Display names (first_name, last_name) using an alias named full_name
SELECT
  first_name || ' ' || last_name AS full_name
FROM customer;

-- B3) All create_date values (no duplicates)
SELECT DISTINCT create_date
FROM customer;

-- B4) All customer details, descending order by first name
SELECT *
FROM customer
ORDER BY first_name DESC;

-- B5) film_id, title, description, release_year, rental_rate (ascending by rental_rate)
SELECT
  film_id,
  title,
  description,
  release_year,
  rental_rate
FROM film
ORDER BY rental_rate ASC;

-- B6) Address + phone of customers living in the Texas district (address table)
SELECT
  c.customer_id,
  c.first_name,
  c.last_name,
  a.address,
  a.phone
FROM customer c
JOIN address a ON a.address_id = c.address_id
WHERE a.district = 'Texas';

-- B7) All movie details where film_id is either 15 or 150
SELECT *
FROM film
WHERE film_id IN (15, 150);

-- B8) Check if your favorite movie exists (replace YOUR_MOVIE_TITLE)
SELECT
  film_id,
  title,
  description,
  length,
  rental_rate
FROM film
WHERE title = 'YOUR_MOVIE_TITLE';

-- B9) Movies starting with first 2 letters of your favorite movie (replace AB)
SELECT
  film_id,
  title,
  description,
  length,
  rental_rate
FROM film
WHERE title ILIKE 'AB%';

-- B10) Find the 10 cheapest movies (by rental_rate, then title)
SELECT
  film_id,
  title,
  rental_rate
FROM film
ORDER BY rental_rate ASC, title ASC
LIMIT 10;

-- B11) Next 10 cheapest movies (Option A: OFFSET)
SELECT
  film_id,
  title,
  rental_rate
FROM film
ORDER BY rental_rate ASC, title ASC
LIMIT 10 OFFSET 10;

-- B11 BONUS) Next 10 cheapest WITHOUT LIMIT (window function)
-- (Uncomment if you want to use this version instead of OFFSET)
-- SELECT film_id, title, rental_rate
-- FROM (
--   SELECT
--     film_id,
--     title,
--     rental_rate,
--     ROW_NUMBER() OVER (ORDER BY rental_rate ASC, title ASC) AS rn
--   FROM film
-- ) t
-- WHERE rn BETWEEN 11 AND 20
-- ORDER BY rn;

-- B12) Join customer + payment: first/last name + amount + date, ordered by customer_id
SELECT
  c.customer_id,
  c.first_name,
  c.last_name,
  p.amount,
  p.payment_date
FROM customer c
JOIN payment p ON p.customer_id = c.customer_id
ORDER BY c.customer_id ASC, p.payment_date ASC;

-- B13) Movies not in inventory (no inventory rows exist for the film)
SELECT
  f.film_id,
  f.title
FROM film f
LEFT JOIN inventory i ON i.film_id = f.film_id
WHERE i.inventory_id IS NULL
ORDER BY f.film_id;

-- B14) Which city is in which country
SELECT
  ci.city,
  co.country
FROM city ci
JOIN country co ON co.country_id = ci.country_id
ORDER BY co.country ASC, ci.city ASC;

-- B15 BONUS) Sellers performance: customer id + names + amount + date, ordered by staff_id
SELECT
  p.staff_id,
  c.customer_id,
  c.first_name,
  c.last_name,
  p.amount,
  p.payment_date
FROM payment p
JOIN customer c ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC, c.customer_id ASC, p.payment_date ASC;


/* ============================================================
   PART C — PUBLIC DATABASE
   Exercise 1: Bonus (Continuation of XP)
   Assumptions:
   - public.customers(id, first_name, last_name, ...)
   - public.purchases(id, customer_id, item_id, quantity, ...)
   ============================================================ */

-- C1) Fetch the last 2 customers in alphabetical order (A-Z) – exclude id
-- ("last 2 in A-Z" => reverse ordering and LIMIT 2)
SELECT first_name, last_name
FROM public.customers
ORDER BY first_name DESC, last_name DESC
LIMIT 2;

-- C2) Delete all purchases made by Scott
DELETE FROM public.purchases
WHERE customer_id IN (
  SELECT id
  FROM public.customers
  WHERE first_name = 'Scott'
);

-- C3) Does Scott still exist in customers? Try and find him
SELECT *
FROM public.customers
WHERE first_name = 'Scott';

-- C4) Find all purchases; join so Scott’s order appears but customer name is blank
-- Use LEFT JOIN: keep purchases even if customer row is missing
SELECT
  p.*,
  c.first_name,
  c.last_name
FROM public.purchases p
LEFT JOIN public.customers c
  ON c.id = p.customer_id
ORDER BY p.id;

-- C5) Find all purchases; join so Scott’s order will NOT appear
-- Use INNER JOIN: only purchases that have a matching customer
SELECT
  p.*,
  c.first_name,
  c.last_name
FROM public.purchases p
INNER JOIN public.customers c
  ON c.id = p.customer_id
ORDER BY p.id;
