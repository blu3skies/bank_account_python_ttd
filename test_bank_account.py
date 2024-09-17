from bank_account import Bank_account

def test_bank_account_init_has_amout():
    customer1 = Bank_account("Test customer")

    assert customer1.account_name == "Test customer"