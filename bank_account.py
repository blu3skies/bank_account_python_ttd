class Bank_account:
    __account_name = ""
    __balance = 0

    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

#customer1 = Bank_account("Joe e", 100)
customer2 = Bank_account(10, "bobby")

isstring = isinstance(customer2.balance, (float, int)) != False

print(isstring)