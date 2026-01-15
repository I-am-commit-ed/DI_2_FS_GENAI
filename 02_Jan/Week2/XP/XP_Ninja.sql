-- Exercise 1 (Public DB) - Bonus Continuation
-- Assumptions:
-- public.customers(id, first_name, last_name, ...)
-- public.purchases(id, customer_id, item_id, quantity, ...)

-- 1) Fetch the last 2 customers in alphabetical order (A-Z) – exclude id
-- "Last 2 in A-Z" means sort ascending then take the last two => ORDER BY DESC with LIMIT 2
SELECT first_name, last_name
FROM public.customers
ORDER BY first_name DESC, last_name DESC
LIMIT 2;

-- 2) Delete all purchases made by Scott
DELETE FROM public.purchases
WHERE customer_id IN (
  SELECT id
  FROM public.customers
  WHERE first_name = 'Scott'
);

-- 3) Does Scott still exist in customers table? Try and find him
SELECT *
FROM public.customers
WHERE first_name = 'Scott';

-- 4) Find all purchases; join so Scott’s order appears but name fields are blank
-- Use LEFT JOIN to keep all purchases even if there is no matching customer
SELECT
  p.*,
  c.first_name,
  c.last_name
FROM public.purchases p
LEFT JOIN public.customers c
  ON c.id = p.customer_id
ORDER BY p.id;

-- 5) Find all purchases; join so Scott’s order will NOT appear
-- Use INNER JOIN to keep only purchases that have a matching customer
SELECT
  p.*,
  c.first_name,
  c.last_name
FROM public.purchases p
INNER JOIN public.customers c
  ON c.id = p.customer_id
ORDER BY p.id;
