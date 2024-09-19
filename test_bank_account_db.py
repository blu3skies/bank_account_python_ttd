import pytest
import sqlite3
from bank_account import Bank_account

@pytest.fixture(autouse=True)
def setup_db():
    # This will run before each test automatically
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Accounts')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Accounts (
        account_number INTEGER PRIMARY KEY,
        account_name TEXT NOT NULL,
        balance REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def test_new_accounts_updates_db():
    # Create a new account and check if it updates in the database
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    account = Bank_account("Test Account", 50.0)
    
    cursor.execute('SELECT balance FROM Accounts WHERE account_name = ?', ("Test Account",))
    result = cursor.fetchone()
    
    assert result[0] == 50  # Verify the balance was correctly inserted
    
    conn.close()