Q1
SELECT COUNT(*)
FROM FirstTab AS ft
WHERE ft.id NOT IN (
  SELECT id FROM SecondTab WHERE id IS NULL
)


Subquery result = (NULL)

So you’re testing: ft.id NOT IN (NULL)

5 NOT IN (NULL) → UNKNOWN

6 NOT IN (NULL) → UNKNOWN

7 NOT IN (NULL) → UNKNOWN

NULL NOT IN (NULL) → UNKNOWN

No row is TRUE ⇒ COUNT = 0

✅ Output: 0 (confirmed by execution)

Q2
SELECT COUNT(*)
FROM FirstTab AS ft
WHERE ft.id NOT IN (
  SELECT id FROM SecondTab WHERE id = 5
)


Subquery result = (5)

So: ft.id NOT IN (5)

5 NOT IN (5) → FALSE

6 NOT IN (5) → TRUE

7 NOT IN (5) → TRUE

NULL NOT IN (5) → UNKNOWN

Only 6 and 7 pass ⇒ COUNT = 2

✅ Output: 2 (confirmed by execution)

Q3
SELECT COUNT(*)
FROM FirstTab AS ft
WHERE ft.id NOT IN (SELECT id FROM SecondTab)


Subquery result = (5, NULL)

So: ft.id NOT IN (5, NULL)

5 NOT IN (5, NULL) → FALSE (because it is in the list)

6 NOT IN (5, NULL) → UNKNOWN (not equal to 5, but comparison with NULL makes it UNKNOWN)

7 NOT IN (5, NULL) → UNKNOWN

NULL NOT IN (5, NULL) → UNKNOWN

No TRUE rows ⇒ COUNT = 0

✅ Output: 0 (confirmed by execution)

Q4
SELECT COUNT(*)
FROM FirstTab AS ft
WHERE ft.id NOT IN (
  SELECT id FROM SecondTab WHERE id IS NOT NULL
)


Subquery result = (5)

Same logic as Q2:

Only 6 and 7 pass ⇒ COUNT = 2

✅ Output: 2 (confirmed by execution)

Final answers

Q1 = 0

Q2 = 2

Q3 = 0

Q4 = 2