SELECT products.name, 
    CASE 
        WHEN products.type = 'A' THEN 20.0
        WHEN products.type = 'B' THEN 70.0
        WHEN products.type = 'C' THEN 530.5
    END AS price
FROM products
ORDER BY 
    CASE 
        WHEN products.type = 'A' THEN 1
        WHEN products.type = 'B' THEN 2
        WHEN products.type = 'C' THEN 3
    END,
products.id DESC;