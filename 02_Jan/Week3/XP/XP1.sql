/* ============================================================
   DVDRental - Exercise 1 (Languages + Films + New Tables + Reviews)
   ============================================================ */

-- 1) Get a list of all languages
SELECT *
FROM language;


-- 2) List all films joined with their languages
--    Required columns: film title, description, language name
SELECT
  f.title,
  f.description,
  l.name AS language_name
FROM film f
JOIN language l
  ON l.language_id = f.language_id
ORDER BY f.title;


-- 3) Get all languages even if there are no films in those languages
--    Required columns: film title, description, language name
--    Use LEFT JOIN from language -> film so every language appears.
SELECT
  f.title,
  f.description,
  l.name AS language_name
FROM language l
LEFT JOIN film f
  ON f.language_id = l.language_id
ORDER BY l.name, f.title;


-- 4) Create new table new_film (id, name) + insert some films
DROP TABLE IF EXISTS customer_review; -- drop review first because it depends on new_film
DROP TABLE IF EXISTS new_film;

CREATE TABLE new_film (
  id   SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) VALUES
  ('The SQL Avenger'),
  ('Query & Furious'),
  ('Nulls in Paradise');


-- 5) Create customer_review table with constraints and ON DELETE CASCADE
--    If a film is deleted, its review should be automatically deleted.
--    film_id references new_film(id) with ON DELETE CASCADE.
--    language_id references language(language_id).
CREATE TABLE customer_review (
  review_id    SERIAL PRIMARY KEY,
  film_id      INTEGER NOT NULL REFERENCES new_film(id) ON DELETE CASCADE,
  language_id  INTEGER NOT NULL REFERENCES language(language_id),
  title        VARCHAR(255) NOT NULL,
  score        INTEGER NOT NULL CHECK (score BETWEEN 1 AND 10),
  review_text  TEXT,
  last_update  TIMESTAMP NOT NULL DEFAULT NOW()
);


-- 6) Add 2 movie reviews (link to valid film_id + language_id)
--    Use actual existing language_id values from your language table.
--    Tip: In dvdrental, English is often language_id = 1, but verify with:
--    SELECT * FROM language;

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES
  (1, 1, 'Surprisingly fun', 9, 'Fast paced, clean plot, and great twists.'),
  (2, 1, 'Good but not perfect', 7, 'Solid movie, a bit long, still worth it.');


-- 7) Delete a film that has a review from new_film. What happens to customer_review?
--    Because of ON DELETE CASCADE, the related rows in customer_review are deleted automatically.

-- Before: show reviews
SELECT *
FROM customer_review
ORDER BY review_id;

-- Delete the film with id = 1 (it has a review)
DELETE FROM new_film
WHERE id = 1;

-- After: review(s) referencing film_id = 1 should be gone
SELECT *
FROM customer_review
ORDER BY review_id;

-- Optional: show remaining films
SELECT *
FROM new_film
ORDER BY id;
