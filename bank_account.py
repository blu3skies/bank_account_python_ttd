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

cursor.execute('''
CREATE TABLE IF NOT EXISTS Transactions (
    trans_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_account_number INTEGER,  -- NULL allowed
    recipient_account_number INTEGER,  -- NULL allowed
    amount REAL NOT NULL
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

        conn =  sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute(''' 
                       UPDATE Accounts
                       SET balance = ?
                       Where account_number = ? 
                       ''', (self.balance, self.account_number))
        
        cursor.execute(''' 
                       INSERT INTO Transactions (sender_account_number, recipient_account_number, amount)
                       VALUES (?, ?, ?)
                       ''', (None, self.account_number, amount))
        conn.commit()
        conn.close()    

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        else:
            self.balance -= amount

    def transfer(self, amount, recipient_account_number):
        if self.balance < amount:
            raise ValueError("Insufficient balance to make transfer.")
        
        conn =  sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('SELECT balance FROM Accounts WHERE account_number = ?', (recipient_account_number,))
        result = cursor.fetchone()

        if result is None:
            conn.close()
            raise ValueError("Recipient account does not exist.")
        
        recipient_balance = result[0] + amount
        self.balance -= amount

        cursor.execute('UPDATE Accounts SET balance = ? WHERE account_number = ?',(self.balance, self.account_number))
        cursor.execute('UPDATE Accounts SET balance = ? WHERE account_number = ?',(recipient_balance, recipient_account_number))
        cursor.execute('''
                       INSERT INTO Transactions (sender_account_number, recipient_account_number, amount)
                       VALUES (?, ?, ?)
                       ''', (self.account_number, recipient_account_number, amount))
        conn.commit()
        conn.close()

    def summarising(self):
        self.summary = f"Account owner: {self.account_name} - Account Balance: £{self.balance} - Accounts Number: {self.account_number}"

#customer_ronnie = Bank_account("Ronnie")
#customer_peppa = Bank_account("Peppa")
#customer_ronnie.deposit(10)
#print(customer_ronnie.balance)
#peppa_acc_num = customer_peppa.account_number
#print(peppa_acc_num)
#customer_ronnie.transfer(10, peppa_acc_num)
#print(customer_ronnie.balance)
#print(customer_peppa.balance)
