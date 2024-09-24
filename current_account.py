from bank_account import Bank_account
import sqlite3

class Current_account(Bank_account):

    def __init__(self, account_name, balance=0, summary=""):
        super().__init__(account_name, balance, summary)
        self.type = "Current"
        self.account_number = self.generate_savings_account_number()         
        self.update_db_account_type()
        self._create_account_in_db()
    
    def generate_savings_account_number(self):
        unique_part = self.generate_unique_account_number()
        return int(f"{unique_part}03") 

    def update_db_account_type(self):
        conn =  sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE Accounts SET type = ? WHERE account_number = ?',(self.type, self.account_number,))
        conn.commit()
        conn.close()