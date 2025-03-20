SELECT account.id, account.password, MD5(password) AS MD5
FROM account