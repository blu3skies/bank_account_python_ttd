from bank_account import Bank_account
import pytest

customer1 = Bank_account("Test customer", 1, 10)
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
    assert isinstance(customer2.account_number, int) == False

def test_deposit():
    customer1.deposit(5)
    assert customer1.balance == 15

def test_withdraw():
    customer1.withdraw(2)
    assert customer1.balance == 13

def test_withdrawl_to_neg_error():
    customer1.balance = 5
    with pytest.raises(ValueError, match="Insufficient balance"):
        customer1.withdraw(6)
    
def test_account_desciption():
    customer3 = Bank_account("Joe Blogs", 3, 32.73)
    customer3.summarising()
    assert customer3.summary == "Account owner: Joe Blogs - Account Balance: £32.73 - Accounts Number: 3" 

