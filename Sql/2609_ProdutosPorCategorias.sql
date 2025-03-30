SELECT categories.name, SUM(products.amount) AS "sum"
FROM categories
INNER JOIN products ON products.id_categories = categories.id
GROUP BY categories.name;