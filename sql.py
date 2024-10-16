
CREATE_ACCOUNT = "INSERT INTO bank_account (name, balance) VALUES(?,?);"

GET_ACCOUNT = "SELECT * FROM bank_account WHERE account_number = (?);"

GET_ACCOUNT_NUMBER = "SELECT account_number FROM bank_account WHERE account_number = (?)"

GET_BALANCE = "SELECT balance FROM bank_account  WHERE account_number = (?);"

DEPOSIT = "UPDATE bank_account SET balance=balance+(?) WHERE account_number =(?)"

# DEPOSIT = "UPDATE bank_account SET balance=:deposit WHERE account_number =:account_number", {'account_number':account_number, 'deposit':deposit}

WITHDRAW = "UPDATE bank_account SET balance=balance-(?) WHERE account_number = (?) RETURNING balance;"

CLOSE_ACCOUNT = "DELETE from bank_account WHERE account_number = (?)"