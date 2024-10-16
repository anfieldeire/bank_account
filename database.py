import sqlite3


def connection():

    conn = sqlite3.connect('bank_account.db')
    curs = conn.cursor()
    print("connected")
    print(f"curs {curs}")
    return curs


def create_tables(curs):

    print(f"This is c")
    curs.execute(""" CREATE TABLE IF NOT EXISTS bank_account (

    name text,
    account_number integer PRIMARY KEY,
    balance integer
    )""")
    print("table created")


if __name__ == '__main__':
    curs = connection()
    create_tables(curs)



