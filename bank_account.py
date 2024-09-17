class Bank_account:
    __account_name = ""
    __balance = 0
    __account_number = 0

    def __init__(self, account_name, balance, account_number):
        self.account_name = account_name
        self.balance = balance
        self.account_number = account_number
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
#customer1 = Bank_account("Joe e", 100, 1)
#customer2 = Bank_account(10, "bobby")

#isstring = isinstance(customer2.balance, (float, int)) != False
#print(customer1.balance)
