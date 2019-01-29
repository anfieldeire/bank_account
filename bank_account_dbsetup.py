import sqlite3  

conn = sqlite3.connect('bank_account.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS bank_account  (

        name text,
        social integer,
        account_number integer PRIMARY KEY,
        balance integer
        )""")



c.execute("""CREATE TABLE IF NOT EXISTS credit_card (

        name text,
        social integer,
        account_number integer PRIMARY KEY,
        balance integer,
        card_no integer,
        credit_limit integer
        )""")


c.execute("""CREATE TABLE IF NOT EXISTS savings_account (

        name text,
        social integer,
        account_number integer PRIMARY KEY,
        balance integer,
        rate real
        )""")


print(c.fetchall())

conn.commit()
conn.close()
