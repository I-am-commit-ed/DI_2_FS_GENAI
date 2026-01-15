Skip to content
Chat history




You said:
🌟 Exercise 1 : Items and customers
Instructions
We will work on the public database that we created yesterday.

Use SQL to get the following from the database:
All items, ordered by price (lowest to highest).
Items with a price above 80 (80 included), ordered by price (highest to lowest).
The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
All last names (no other columns!), in reverse alphabetical order (Z-A)
ChatGPT said:
I’ll write the exact SQL queries for each requirement (with ORDER BY, filters, and LIMIT), assuming typical items and customers tables in your public schema.

Here are the SQL queries (PostgreSQL) for each ask, assuming tables public.items and public.customers.

1) All items, ordered by price (lowest → highest)
SELECT *
FROM public.items
ORDER BY price ASC;
2) Items with price ≥ 80, ordered by price (highest → lowest)
SELECT *
FROM public.items
WHERE price >= 80
ORDER BY price DESC;
3) First 3 customers alphabetically by first name (A–Z), excluding the primary key column
(assuming the PK column is id)

SELECT first_name, last_name
FROM public.customers
ORDER BY first_name ASC
LIMIT 3;
4) All last names only, reverse alphabetical order (Z–A)
SELECT last_name
FROM public.customers
ORDER BY last_name DESC;
You said:
🌟 Exercise 2 : dvdrental database
Instructions
Setup
We will install a new sample database on our PostgreSQL servers.
Download this sample database file

There is a single file called dvdrental.tar inside the zip. Extract it to your local directory.
Tip : If you are using Mac, after extracting the zip file you will get a folder called dvdrental

Go to pgAdmin4, and navigate to Databases on the left panel.

Right click > Create > Database…

Type in the name of the new database: dvdrental, and click Save. Wait a few moments.

Right click on dvdrental under Databases in the left panel.

Click Restore….

For PC users choose the following format Custom or tar. For Mac Users, choose the following format Directory.

Next to Filename, you should see a button with 3 dots on it. Click the button.

For PC users: “Find your file in the window”. For Max users: “Find your folder in the window”. (you may have to check Show hidden files and folders?), and click the Select button.


If you get errors:
If you receive a “Utility not found” Error, you need to change pgadmin binary path. Check out this video

If you receive an error of binary path :
Go to your computer documents -> C: (on windows) -> Program Files -> PostgreSQL -> your version -> bin. Copy this path, it should be something like this : C:\Program Files\PostgreSQL\15\bin.
In pgAdmin select File -> Preferences -> Path -> Binary Path -> scroll down to PostgreSQL Binary Path -> Find your PostgreSQL version -> paste the path -> Save

If you see any other error messages, please save them and get assistance. If not, you should have a new database loaded into your server!
If you have a problem importing the database, here are the DEFAULT instructions


Diagram of the tables
Here is a diagram of the tables in the server. Take a look at it and learn about the tables, their columns, and the relationships between the different tables.



diagram



We will use the newly installed dvdrental database.

In the dvdrental database write a query to select all the columns from the “customer” table.

Write a query to display the names (first_name, last_name) using an alias named “full_name”.

Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).

Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.

Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

Write a query to retrieve all movie details where the movie id is either 15 or 150.

Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.

No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.

Write a query which will find the 10 cheapest movies.

Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
Bonus: Try to not use LIMIT.

Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).

You need to check your inventory. Write a query to get all the movies which are not in inventory.

Write a query to find which city is in which country.

Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
ChatGPT said:
I’ll give you the exact SQL for each dvdrental question (PostgreSQL), including joins, ordering, and the “next 10 cheapest” version both with OFFSET and a no-LIMIT window-function approach.

Below are PostgreSQL queries for each task in the dvdrental database.

1) Select all columns from customer
SELECT *
FROM customer;
2) Display names as full_name (alias)
SELECT
  first_name || ' ' || last_name AS full_name
FROM customer;
3) All account creation dates (no duplicates)
SELECT DISTINCT create_date
FROM customer;
4) All customer details, descending by first name
SELECT *
FROM customer
ORDER BY first_name DESC;
5) Film id, title, description, release year, rental rate ordered by rental_rate ASC
SELECT
  film_id,
  title,
  description,
  release_year,
  rental_rate
FROM film
ORDER BY rental_rate ASC;
6) Address + phone of customers living in Texas district (address table)
In dvdrental, customers link to address via customer.address_id.

SELECT
  c.customer_id,
  c.first_name,
  c.last_name,
  a.address,
  a.phone
FROM customer c
JOIN address a ON a.address_id = c.address_id
WHERE a.district = 'Texas';
7) All movie details where movie id is 15 or 150
SELECT *
FROM film
WHERE film_id IN (15, 150);
8) Check if your favorite movie exists (exact title match)
Replace YOUR_MOVIE_TITLE with your movie title.

SELECT
  film_id,
  title,
  description,
  length,
  rental_rate
FROM film
WHERE title = 'YOUR_MOVIE_TITLE';
9) If not found: movies starting with first 2 letters of your favorite movie
Replace AB with the first two letters.

SELECT
  film_id,
  title,
  description,
  length,
  rental_rate
FROM film
WHERE title ILIKE 'AB%';
10) Find the 10 cheapest movies
Cheapest = lowest rental_rate (and tie-break by title).

SELECT
  film_id,
  title,
  rental_rate
FROM film
ORDER BY rental_rate ASC, title ASC
LIMIT 10;
11) Next 10 cheapest movies
Option A (simple): OFFSET
SELECT
  film_id,
  title,
  rental_rate
FROM film
ORDER BY rental_rate ASC, title ASC
LIMIT 10 OFFSET 10;
Option B (bonus, no LIMIT): window function
SELECT film_id, title, rental_rate
FROM (
  SELECT
    film_id,
    title,
    rental_rate,
    ROW_NUMBER() OVER (ORDER BY rental_rate ASC, title ASC) AS rn
  FROM film
) t
WHERE rn BETWEEN 11 AND 20
ORDER BY rn;
12) Join customer + payment: names + amount + payment date, ordered by customer id
SELECT
  c.customer_id,
  c.first_name,
  c.last_name,
  p.amount,
  p.payment_date
FROM customer c
JOIN payment p ON p.customer_id = c.customer_id
ORDER BY c.customer_id ASC, p.payment_date ASC;
13) Movies not in inventory
In dvdrental, inventory rows represent physical copies. Films with no inventory rows are “not in inventory”.

SELECT
  f.film_id,
  f.title
FROM film f
LEFT JOIN inventory i ON i.film_id = f.film_id
WHERE i.inventory_id IS NULL
ORDER BY f.film_id;
14) Which city is in which country
City → Country goes through city.country_id.

SELECT
  ci.city,
  co.country
FROM city ci
JOIN country co ON co.country_id = ci.country_id
ORDER BY co.country, ci.city;
15) Bonus: see sellers performance (staff who sold)
Get customer id + names + amount + date, ordered by staff id

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
If you want, paste your favorite movie title and I’ll write the exact #8 and #9 using it.

You said:
give me all this 15 in one file that I can copy paste
ChatGPT said:
-- DVDrental Exercise 2 (PostgreSQL) - All 15 queries in one file

-- 1) Select all columns from customer
SELECT *
FROM customer;

-- 2) Display names (first_name, last_name) as full_name
SELECT
  first_name || ' ' || last_name AS full_name
FROM customer;

-- 3) All create_date values (no duplicates)
SELECT DISTINCT create_date
FROM customer;

-- 4) All customer details ordered by first_name DESC
SELECT *
FROM customer
ORDER BY first_name DESC;

-- 5) Film ID, title, description, release year, rental rate ordered by rental_rate ASC
SELECT
  film_id,
  title,
  description,
  release_year,
  rental_rate
FROM film
ORDER BY rental_rate ASC;

-- 6) Address + phone of customers living in Texas district
SELECT
  c.customer_id,
  c.first_name,
  c.last_name,
  a.address,
  a.phone
FROM customer c
JOIN address a ON a.address_id = c.address_id
WHERE a.district = 'Texas';

-- 7) Movie details where film_id is 15 or 150
SELECT *
FROM film
WHERE film_id IN (15, 150);

-- 8) Check if your favorite movie exists (replace YOUR_MOVIE_TITLE)
SELECT
  film_id,
  title,
  description,
  length,
  rental_rate
FROM film
WHERE title = 'YOUR_MOVIE_TITLE';

-- 9) Movies starting with first 2 letters of your favorite movie (replace AB)
SELECT
  film_id,
  title,
  description,
  length,
  rental_rate
FROM film
WHERE title ILIKE 'AB%';

-- 10) 10 cheapest movies (by rental_rate, then title)
SELECT
  film_id,
  title,
  rental_rate
FROM film
ORDER BY rental_rate ASC, title ASC
LIMIT 10;

-- 11) Next 10 cheapest movies (Option A: OFFSET)
SELECT
  film_id,
  title,
  rental_rate
FROM film
ORDER BY rental_rate ASC, title ASC
LIMIT 10 OFFSET 10;

-- 12) Join customer + payment: names, amount, date ordered by customer_id
SELECT
  c.customer_id,
  c.first_name,
  c.last_name,
  p.amount,
  p.payment_date
FROM customer c
JOIN payment p ON p.customer_id = c.customer_id
ORDER BY c.customer_id ASC, p.payment_date ASC;

-- 13) Movies not in inventory (no inventory rows)
SELECT
  f.film_id,
  f.title
FROM film f
LEFT JOIN inventory i ON i.film_id = f.film_id
WHERE i.inventory_id IS NULL
ORDER BY f.film_id;

-- 14) Which city is in which country
SELECT
  ci.city,
  co.country
FROM city ci
JOIN country co ON co.country_id = ci.country_id
ORDER BY co.country, ci.city;

-- 15) Bonus: customers + payments ordered by staff_id (seller)
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


-- Bonus (from #11): Next 10 cheapest WITHOUT LIMIT (window function)
-- Uncomment if you want to use this version instead of OFFSET.
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




No file chosenNo file chosen
ChatGPT is AI and can make mistakes. Check important info.
