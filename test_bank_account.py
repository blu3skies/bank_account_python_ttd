from bank_account import Bank_account

def test_bank_account_init_has_name():
    customer1 = Bank_account("Test customer", 10)

    assert customer1.account_name == "Test customer"

def test_account_has_balance():
    customer2 = Bank_account("Test Test", 10)
    assert customer2.balance == 10