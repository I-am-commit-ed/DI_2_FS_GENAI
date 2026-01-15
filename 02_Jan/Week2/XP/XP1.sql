SELECT *
FROM public.items
ORDER BY price ASC;


SELECT *
FROM public.items
WHERE price >= 80
ORDER BY price DESC;


SELECT first_name, last_name
FROM public.customers
ORDER BY first_name ASC
LIMIT 3;


SELECT last_name
FROM public.customers
ORDER BY last_name DESC;
