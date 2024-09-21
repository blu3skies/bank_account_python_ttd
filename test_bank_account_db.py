import pytest
import sqlite3
from bank_account import Bank_account

@pytest.fixture(autouse=True)
def setup_db():
    # This will run before each test automatically
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Accounts')
    cursor.execute('DROP TABLE IF EXISTS Transactions')
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
        sender_account_number INTEGER,  
        recipient_account_number INTEGER NOT NULL,
        amount REAL NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

def test_new_accounts_updates_db():
    # Create a new account and check if it updates in the database
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    account = Bank_account("Test Account", 50.0)
    
    cursor.execute('SELECT balance FROM Accounts WHERE account_name = ?', (account.account_name,))
    result = cursor.fetchone()
    
    assert result[0] == 50  # Verify the balance was correctly inserted
    
    conn.close()

def test_deposit_updates_accounts_db():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    customer1 = Bank_account("Ronnie", 10)

    customer1.deposit(21)
    acc_num = customer1.account_number

    cursor.execute('SELECT balance FROM Accounts WHERE account_number = ?', (acc_num,))
    result = cursor.fetchone()
    assert result[0] == 31
    conn.close()

def test_transfer():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    ronnie = Bank_account("Ronnie", 10)
    peppa = Bank_account("Peppa", 0)

    ronnie.transfer(10, peppa.account_number)

    cursor.execute('SELECT balance FROM Accounts WHERE account_number = ?', (ronnie.account_number,))
    result = cursor.fetchone()
    assert result[0] == 0

    cursor.execute('SELECT balance FROM Accounts WHERE account_number = ?', (peppa.account_number,))
    result = cursor.fetchone()
    assert result[0] == 10
    conn.close()

def test_transfer_db():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    ronnie = Bank_account("Ronnie", 50)
    peppa = Bank_account("Peppa", 10)

    peppa.transfer(10, ronnie.account_number)

    cursor.execute('SELECT sender_account_number FROM Transactions WHERE recipient_account_number = ?', (ronnie.account_number,))
    result = cursor.fetchone()
    assert int(result[0]) == peppa.account_number

    cursor.execute('SELECT recipient_account_number FROM Transactions WHERE sender_account_number = ?', (peppa.account_number,))
    result = cursor.fetchone()
    assert int(result[0]) == ronnie.account_number

    cursor.execute('SELECT amount FROM Transactions WHERE recipient_account_number = ?', (ronnie.account_number,))
    result = cursor.fetchone()
    assert int(result[0]) == 10

    cursor.execute('SELECT amount FROM Transactions WHERE recipient_account_number = ?', (ronnie.account_number,))
    result = cursor.fetchone()
    assert result[0] != None
    conn.close()

def test_deposit_updates_transactions_db():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    bentley = Bank_account("Bentley")
    bentley.deposit(1000)

    cursor.execute('SELECT amount FROM Transactions WHERE recipient_account_number = ? ', (bentley.account_number,))
    result = cursor.fetchone()
    assert result[0] == 1000
    conn.close()