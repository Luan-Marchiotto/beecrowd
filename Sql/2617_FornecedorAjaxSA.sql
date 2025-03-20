SELECT products.name,providers.name 
FROM products 
INNER join providers on providers.id=products.id_providers
WHERE providers.name='Ajax SA';