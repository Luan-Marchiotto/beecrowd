SELECT products.name, providers.name, products.price
FROM products
INNER JOIN providers ON providers.id = products.id_providers
INNER JOIN categories ON categories.id = products.id_categories 
WHERE products.price > 1000 
AND categories.name = 'Super Luxury';