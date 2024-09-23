from bank_account import Bank_account
import sqlite3

class Savings_account(Bank_account):
    __type = ""
    

    def __init__(self, account_name, balance=0, summary=""):
        super().__init__(account_name, balance, summary)
        self.type = "Savings"
        self.account_number = self.generate_savings_account_number()         
        self.update_db_account_type()
        self._create_account_in_db()
    
    def generate_savings_account_number(self):
        unique_part = self.generate_unique_account_number()
        return int(f"{unique_part}02") 

    def update_db_account_type(self):
        conn =  sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE Accounts SET type = ? WHERE account_number = ?',(self.type, self.account_number,))
        conn.commit()
        conn.close()

    def apply_interest(self):
        current_interest_rate = 0.06
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('SELECT balance from Accounts WHERE account_number = ?', (self.account_number,))
        result = cursor.fetchone()
        new_balance = int(result[0])*current_interest_rate + int(result[0])
        print(new_balance)
        cursor.execute('UPDATE Accounts SET balance = ? WHERE account_number = ?', (new_balance, self.account_number))
        conn.commit()
        conn.close()

joe = Savings_account("joe")
print(joe.account_number)
#print(str(joe.account_number).endswith("02"))