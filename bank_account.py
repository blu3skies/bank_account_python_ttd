import sqlite3
import random

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

    def __init__(self, account_name, balance=0.00, summary=""):
        self.account_name = account_name
        self.balance = balance
        self.account_number = self.generate_unique_account_number()
        self.summary = summary

        # When the account is created, automatically insert it into the database
        self._create_account_in_db()

    def generate_unique_account_number(self):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()

        while True:
            account_number = random.randint(100000, 999999)
            print(account_number)
            cursor.execute('SELECT account_number FROM Accounts WHERE Account_number = ?', (account_number,))
            result = cursor.fetchone()

            if not result: 
                conn.close()
                return account_number
    
    def _create_account_in_db(self):
        conn =  sqlite3.connect('bank.db')
        cursor = conn.cursor()

        #print(f"Inserting account: {self.account_number}, {self.account_name}, {self.balance}")

        cursor.execute('''
                       INSERT INTO Accounts (account_number, account_name, balance)
                       VALUES (?, ?, ?)
                       ''', (self.account_number, self.account_name, self.balance))
        conn.commit()
        conn.close()

    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        else:
            self.balance -= amount

    def summarising(self):
        self.summary = f"Account owner: {self.account_name} - Account Balance: £{self.balance} - Accounts Number: {self.account_number}"

#customer3 = Bank_account("Joe Blogs", 32.73)

#customer2 = Bank_account(10, "bobby")
#isstring = isinstance(customer2.balance, (float, int)) != False

#customer3.summarising()
#print(customer3.account_number)
#print("Account owner: Joe Blogs - Account Balance: £32.73 - Accounts Number: 3")