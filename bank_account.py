import sqlite3
from sql import CREATE_ACCOUNT, GET_BALANCE, DEPOSIT, WITHDRAW, CLOSE_ACCOUNT
from database import connection

conn = sqlite3.connect('bank_account.db')
curs = conn.cursor()


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    def create_account(self, name, balance):
        ''' Create a bank account. Acct number auto increments. '''

        with conn:
            result = curs.execute(CREATE_ACCOUNT, (name, balance))
            print(f"Account number: {result.lastrowid} created")


    def get_balance(self, account_number):
        ''' Input account number. Return balance of the account. '''

        with conn:
            balance =  curs.execute(GET_BALANCE, (account_number)).fetchone()
            print(f"Balance for account number: {account_number} is {balance[0]}")


    def deposit(self, account_number, deposit):
        ''' Accept account number and deposit '''

        with conn:
            result = curs.execute(DEPOSIT, (deposit, account_number)).fetchone()
            print(f"Deposit of {deposit} made for account: {account_number} ")

    def withdraw(self, account_number, amount):
        ''' Accept account number and withdrawl amount. Make sure the account has enough for the withdrawl'''

        with conn:
            balance = curs.execute(GET_BALANCE, (account_number)).fetchone()
            curr_balance = balance[0]
            if curr_balance - amount >= 0:
                balance = curs.execute(WITHDRAW, (amount, account_number)).fetchone()
                print(f"Balance after withdrawl of {amount} is now: {balance[0]}")
            else:
                print(f"Insufficient balance")

    def close_account(self, account_number):
        ''' Close customer acct by deleting the record from DB
            No rows means no match for the provided acct number '''

        with conn:
            result = curs.execute(CLOSE_ACCOUNT, account_number).fetchone()
            rowcount = curs.rowcount
            if rowcount == 1:
                print(f"Account number {account_number} has been closed")
            else:
                print(f"Account number {account_number} does not exist. Try again")



if __name__ == "__main__":


    Troy = BankAccount("Troy B", 100)
    Troy.close_account('7')



