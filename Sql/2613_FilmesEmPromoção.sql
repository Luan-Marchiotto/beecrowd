SELECT movies.id, movies.name 
FROM movies
INNER JOIN prices ON prices.id = movies.id_prices
WHERE prices.value <2.00;