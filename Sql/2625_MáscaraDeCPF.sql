SELECT CONCAT(
    SUBSTRING(natural_person.cpf, 1, 3), '.', 
    SUBSTRING(natural_person.cpf, 4, 3), '.', 
    SUBSTRING(natural_person.cpf, 7, 3), '-', 
    SUBSTRING(natural_person.cpf, 10, 2)
  ) AS CPF
FROM customers
INNER JOIN natural_person ON natural_person.id_customers = customers.id;