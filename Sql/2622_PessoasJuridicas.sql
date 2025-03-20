SELECT customers.name
FROM customers
INNER JOIN legal_person ON legal_person.id_customers = customers.id