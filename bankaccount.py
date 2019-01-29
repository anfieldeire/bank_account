import sqlite3

conn = sqlite3.connect('bank_account.db')

c = conn.cursor()        


class BankAccount:

    def __init__(self, name, social, account_number, balance):
        self.name = name
        self.social = social
        self.account_number = account_number
        self.balance = balance


    @classmethod
    def get_account(cls, acc):
        with conn:
            account_find = c.execute("SELECT * from bank_account WHERE account_number=:account_number", {'account_number':
                        acc})
            account_found = c.fetchone()
            if not account_found:
                print("No account matching that number could be found")

            else:
                print("Account exists!")
                print(account_found)
        return(account_found)         
    conn.commit()

    @classmethod
    def create_account(cls, name, social, account_number, balance):      
        with conn:
            account_found = BankAccount.get_account(account_number)
            if not account_found:
                    
                c.execute("INSERT INTO bank_account VALUES (:name, :social, :account_number, :balance)",
                          {'name':name, 'social': social,'account_number': account_number, 'balance':balance})  
                print("New Account {} has been created".format(account_number))
            else:
                pass
        conn.commit()
        
    @classmethod
    def deposit(cls, account_number, amount):
        with conn:
            account_found = BankAccount.get_account(account_number)
            if account_found:
                existing_bal = account_found[3]
                c.execute("""UPDATE bank_account SET balance=balance +:amount
                        WHERE account_number =:account_number""",
                          {'account_number':account_number, 'amount':amount})
                print("${} has been deposited to account {} and the new balance is ${}".format(amount, account_number, existing_bal + amount))
            else:
                pass
            
    @classmethod        
    def withdraw(clas, account_number, amount):
        with conn:
            account_found = BankAccount.get_account(account_number)
            if amount > account_found[3]:
                print("You do not have enough funds")
            else:    
                existing_bal = account_found[3]
                c.execute("""UPDATE bank_account SET balance=balance -:amount
                        WHERE account_number =:account_number""",
                          {'account_number':account_number, 'amount':amount})
                print("${} has been withdrawn from account {} and the new balance is ${}".format(amount, account_number, existing_bal - amount))

class SavingsAccount(BankAccount):
    def __init__(self, name, social, account_number, balance, rate):
        super().__init__(name, social, account_number, balance)
        self.rate = rate

    @classmethod
    def get_account(cls, acc):
        with conn:
            account_find = c.execute("SELECT * from savings_account WHERE account_number=:account_number", {'account_number':
                        acc})
            account_found = c.fetchone()
            if not account_found:
                print("No savings account matching that number could be found")

            else:
                print("Savings Account exists!")
                print(account_found)
        return(account_found)    

    @classmethod
    def create_account(cls, name, social, account_number, balance, rate):    
        with conn:
            account_found = SavingsAccount.get_account(account_number)
            if not account_found:
                    
                c.execute("INSERT INTO savings_account VALUES (:name, :social, :account_number, :balance, :rate)",
                          {'name':name, 'social': social,'account_number': account_number, 'balance':balance, 'rate':rate})  
                print("from savings account object")
                print("New Account {} has been created".format(account_number))

        conn.commit()

    @classmethod
    def get_account(cls, account_number):
        account_found = SavingsAccount.get_account(account_number) 


class CreditCard(BankAccount):
    def __init__(self, name, social, account_number, balance, credit_score, credit_limit):
        super().__init__(name, social, account_number, balance)
        self.credit_score = credit_score
        self.credit_limit = credit_limit


    @classmethod
    def create_account(cls, name, social, account_number, balance, credit_score, credit_limit):       
        with conn:
#            account_found = CreditCard.get_account(account_number)
#            print(account_found)
#            if not account_found:
                
            c.execute("INSERT INTO credit_card VALUES (:name, :social, :account_number, :balance, :credit_score, :credit_limit)",
                      {'name':name, 'social': social,'account_number': account_number, 'balance':balance, 'credit_score':credit_score,
                       'credit_limit':credit_limit})  
            print("From credit card object")
            print("New credit card account {} has been created".format(account_number))
            
        conn.commit()


    @classmethod
    def deposit(cls, account_number, amount):
#            if account_found:
#                existing_bal = account_found[3]
        c.execute("""UPDATE credit_card SET balance=balance +:amount
                WHERE account_number =:account_number""",
                  {'account_number':account_number, 'amount':amount})
        print("${} has been deposited to account {}".format(amount, account_number))

        


if __name__ == '__main__':
#    SavingsAccount.create_account("Robbie Mustoe", 135063022, 7888, 800.00, 2)
#    CreditCard.create_account('Joey Brien', 2234, 55544, -400.00, 600, -1000.00)
    CreditCard.deposit(55544, 200)
#    BankAccount.withdraw(145000, 200.00)
"""
#    BankAccount.withdraw(145000,3000.00)
    SavingsAccount.create_account("Robbie Mustoe", 135063022, 16244432, 800.00, 2)
    issubclass(SavingsAccount, BankAccount)
    b = BankAccount('Frank Carson', 223, 66554, 200.00)
    print(b.name)
    ghsav = SavingsAccount('George Groves', 224, 77889, 100.00, 2)
    print(ghsav.get_account)
    print(ghsav.rate)
    print(isinstance(ghsav, BankAccount))
    print(issubclass(SavingsAccount, BankAccount))
    
#SavingsAccount.get_account(15044432)
#    BankAccount.name= 'Sam Sammy'
#    conn.close() 

"""
                                                                                      



        
