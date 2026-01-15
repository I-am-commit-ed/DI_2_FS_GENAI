SELECT COUNT(*) AS actor_count
FROM actors;

INSERT INTO actors (first_name, last_name, birth_date)
VALUES (NULL, 'Doe', '2000-01-01');

SELECT column_name, is_nullable
FROM information_schema.columns
WHERE table_name = 'actors';



