from bank_account import Bank_account
import pytest
import sqlite3

def test_new_accounts_updates_db():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    account = Bank_account("Test Account", 1, 50.0)

    cursor.execute('SELECT balance FROM Accounts WHERE account_number = ?', (1))
    result = cursor.fetchone()

    assert result[0] == 50

    conn.close()