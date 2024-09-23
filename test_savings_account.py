import pytest
import sqlite3
from savings_account import Savings_account

@pytest.fixture(autouse=True)
def setup_db():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    # Drop and recreate the tables
    cursor.execute('DROP TABLE IF EXISTS Accounts')
    cursor.execute('DROP TABLE IF EXISTS Transactions')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Accounts (
        account_number INTEGER PRIMARY KEY,
        type TEXT, -- NULL allowed
        account_name TEXT NOT NULL,
        balance REAL NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transactions (
        trans_id INTEGER PRIMARY KEY AUTOINCREMENT,
        transaction_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        sender_account_number INTEGER,  -- NULL allowed
        recipient_account_number INTEGER,  -- NULL allowed
        amount REAL NOT NULL
    )
    ''')

def test_create_savings_account():

    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    bridie = Savings_account("Bridie")

    cursor.execute('SELECT type FROM Accounts WHERE account_number = ?', (bridie.account_number,))
    result = cursor.fetchone()
    print(result)


    assert result[0] == "Savings"

#def test_add_interest_rate_to_balance():
#    
#    conn = sqlite3.connect('bank.db')
#    cursor = conn.cursor()
#    
#    bridie = Savings_account("Bridie")
#    print(bridie.type)
#
#    bridie.deposit(100)
#    bridie.apply_interest()
#
#    cursor.execute('SELECT balance FROM Accounts WHERE account_number = ?', (bridie.account_number,))
#    result = cursor.fetchone()
#
#    assert result[0] == 106
#

