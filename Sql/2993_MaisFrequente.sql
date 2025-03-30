SELECT value_table.amount AS most_frequent_value
FROM value_table
GROUP BY value_table.amount
ORDER BY COUNT(value_table.amount) DESC
LIMIT 1;