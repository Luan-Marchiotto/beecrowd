SELECT life_registry.name, ROUND(life_registry.omega * 1.618, 3) AS "Fator N"
FROM life_registry
INNER JOIN dimensions ON life_registry.dimensions_id = dimensions.id
WHERE life_registry.name LIKE 'Richard%'
AND dimensions.name IN ('C774', 'C875')
ORDER BY life_registry.omega ASC;