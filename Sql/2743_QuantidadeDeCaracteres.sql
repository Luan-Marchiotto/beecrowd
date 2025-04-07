SELECT people.name, LENGTH(people.name) AS "length"
FROM people
ORDER BY length DESC;