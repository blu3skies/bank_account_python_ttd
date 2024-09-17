from bank_account import Bank_account

customer1 = Bank_account("Test customer", 10, 1)
customer2 = Bank_account(10, "bobby", "2")

def test_bank_account_init_has_name():
    assert customer1.account_name == "Test customer"

def test_bank_account_name_is_string():
    assert isinstance(customer1.account_name,str)
    assert isinstance(customer2.account_name,str) == False
def test_account_has_balance():
    assert customer1.balance == 10

def test_account_balance_is_float_or_int():
    assert isinstance(customer1.balance, (float, int))
    assert isinstance(customer2.balance, (float, int)) == False

def test_account_number():
    assert customer1.account_number == 1

def test_account_number_is_int():
    assert isinstance(customer1.account_number, int)