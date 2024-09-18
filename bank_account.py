import sqlite3
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Accounts (
    account_number INTEGER PRIMARY KEY,
    account_name TEXT NOT NULL,
    balance REAL NOT NULL
)
''')

class Bank_account:
    __account_name = ""
    __balance = 0
    __account_number = 0
    __summary = ""

    def __init__(self, account_name, account_number, balance=0.00, summary=""):
        self.account_name = account_name
        self.balance = balance
        self.account_number = account_number
        self.summary = summary
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        else:
            self.balance -= amount

    def summarising(self):
        self.summary = f"Account owner: {self.account_name} - Account Balance: £{self.balance} - Accounts Number: {self.account_number}"

#customer3 = Bank_account("Joe Blogs", 3, 32.73)

#customer2 = Bank_account(10, "bobby")
#isstring = isinstance(customer2.balance, (float, int)) != False

#customer3.summarising()
#print(customer3.summary == "Account owner: Joe Blogs - Account Balance: £32.73 - Accounts Number: 3")
#print("Account owner: Joe Blogs - Account Balance: £32.73 - Accounts Number: 3")