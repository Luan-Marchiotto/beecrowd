SELECT products.id, products.name
FROM products
INNER JOIN categories ON categories.id = products.id_categories
WHERE categories.name ILIKE 'super%';