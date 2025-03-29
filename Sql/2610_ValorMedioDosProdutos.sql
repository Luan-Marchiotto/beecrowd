SELECT ROUND(SUM(products.price) / COUNT(DISTINCT products.id), 2) AS price
FROM products;