SELECT loan.name, 
    CAST(EXTRACT(DAY FROM loan.payday) AS INT) AS day
FROM loan;