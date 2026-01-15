/* ============================================================
   DVDRental - Exercise 2 (All answers in one file)
   ============================================================ */

---------------------------------------------------------------
-- 1) UPDATE: change the language of some films (valid languages)
---------------------------------------------------------------
-- See valid languages first
SELECT language_id, name
FROM language
ORDER BY language_id;

-- Example: set a few films to a valid language_id (pick IDs that exist)
-- NOTE: adjust language_id numbers based on the SELECT above.
UPDATE film
SET language_id = 2
WHERE film_id IN (1, 2, 3);

UPDATE film
SET language_id = 3
WHERE film_id IN (4, 5, 6);

-- Verify changes
SELECT film_id, title, language_id
FROM film
WHERE film_id IN (1,2,3,4,5,6)
ORDER BY film_id;


--------------------------------------------------------------------
-- 2) Foreign keys (references) defined for the customer table
--    + how it affects INSERT into customer
--------------------------------------------------------------------
-- Show FKs on customer table (the actual source of truth)
SELECT
  tc.constraint_name,
  kcu.column_name,
  ccu.table_name AS references_table,
  ccu.column_name AS references_column
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
  AND tc.table_schema = kcu.table_schema
JOIN information_schema.constraint_column_usage ccu
  ON ccu.constraint_name = tc.constraint_name
  AND ccu.table_schema = tc.table_schema
WHERE tc.table_schema = 'public'
  AND tc.table_name = 'customer'
  AND tc.constraint_type = 'FOREIGN KEY'
ORDER BY tc.constraint_name;

-- In dvdrental, customer.address_id references address(address_id).
-- This means when you INSERT a customer, address_id must already exist in address.
-- Example INSERT pattern (DO NOT run unless you want to add a customer):
-- 1) find a valid address_id first:
-- SELECT address_id FROM address ORDER BY address_id LIMIT 1;
-- 2) then insert using that address_id:
-- INSERT INTO customer (store_id, first_name, last_name, email, address_id, activebool, create_date)
-- VALUES (1, 'Test', 'Customer', 'test@example.com', <VALID_ADDRESS_ID>, TRUE, CURRENT_DATE);


---------------------------------------------------------------
-- 3) Drop customer_review table. Easy or extra checking?
---------------------------------------------------------------
-- If other tables depend on customer_review, DROP will fail unless you CASCADE.
-- Safe approach: try normal drop, or use CASCADE if you know it’s ok.

DROP TABLE IF EXISTS customer_review;

-- If it fails due to dependencies, use:
-- DROP TABLE IF EXISTS customer_review CASCADE;


---------------------------------------------------------------
-- 4) How many rentals are still outstanding (not returned yet)?
---------------------------------------------------------------
-- Outstanding = return_date IS NULL
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;


---------------------------------------------------------------
-- 5) 30 most expensive movies which are outstanding (not returned)
---------------------------------------------------------------
-- Define "most expensive" as highest replacement_cost (DVD replacement price).
-- Join: rental -> inventory -> film
SELECT
  f.film_id,
  f.title,
  f.rental_rate,
  f.replacement_cost,
  r.rental_id,
  r.rental_date
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC, f.rental_rate DESC, f.title ASC
LIMIT 30;


---------------------------------------------------------------
-- 6) Help find the 4 movies (mystery film queries)
---------------------------------------------------------------

-- 6.1) Film about a sumo wrestler, and one actor is Penelope Monroe
-- Join: film -> film_actor -> actor
-- Filter by actor name + keyword "sumo" in description (and/or title)
SELECT DISTINCT
  f.film_id,
  f.title,
  f.description
FROM film f
JOIN film_actor fa ON fa.film_id = f.film_id
JOIN actor a ON a.actor_id = fa.actor_id
WHERE a.first_name = 'PENELOPE'
  AND a.last_name  = 'MONROE'
  AND (f.description ILIKE '%sumo%' OR f.title ILIKE '%sumo%')
ORDER BY f.title;

-- 6.2) Short documentary (< 60 minutes), rated 'R'
SELECT
  film_id,
  title,
  description,
  length,
  rating
FROM film
WHERE length < 60
  AND rating = 'R'
  AND (description ILIKE '%documentary%' OR title ILIKE '%documentary%')
ORDER BY length ASC, title ASC;

-- 6.3) Film that Matthew Mahan rented.
--      He paid > $4.00, and returned it between July 28 and Aug 1, 2005.
-- Join: customer -> rental -> payment -> inventory -> film
SELECT DISTINCT
  f.film_id,
  f.title,
  f.rental_rate,
  p.amount,
  r.return_date,
  c.first_name,
  c.last_name
FROM customer c
JOIN rental r   ON r.customer_id = c.customer_id
JOIN payment p  ON p.rental_id = r.rental_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f     ON f.film_id = i.film_id
WHERE c.first_name = 'MATTHEW'
  AND c.last_name  = 'MAHAN'
  AND p.amount > 4.00
  AND r.return_date >= DATE '2005-07-28'
  AND r.return_date <  DATE '2005-08-02'  -- inclusive through Aug 1
ORDER BY r.return_date ASC, p.amount DESC, f.title;

-- 6.4) Another film Matthew Mahan watched:
--      has word "boat" in title OR description,
--      and looks expensive to replace (high replacement_cost).
SELECT DISTINCT
  f.film_id,
  f.title,
  f.description,
  f.replacement_cost
FROM customer c
JOIN rental r    ON r.customer_id = c.customer_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f      ON f.film_id = i.film_id
WHERE c.first_name = 'MATTHEW'
  AND c.last_name  = 'MAHAN'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC, f.title ASC;
