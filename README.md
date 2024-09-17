This project is something I have come up with with the help of ChatGPT as a general refresher in TTD using classes etc. 

### Project Brief: **Bank Account Management System**

#### Objective:
The goal of this project is to build a **Bank Account Management System** using object-oriented programming (OOP) principles and Test-Driven Development (TDD). The system will allow users to create and manage different types of bank accounts (such as Savings and Current accounts), make deposits, withdrawals, transfers, and apply interest. The system should also allow the bank to manage multiple accounts.

#### Requirements:

1. **Account Class**:
   - Attributes:
     - `account_number`: A unique identifier for the account.
     - `owner_name`: The name of the account owner.
     - `balance`: The current balance of the account.
   - Methods:
     - `deposit(amount)`: Adds the specified amount to the account balance. The amount must be greater than zero.
     - `withdraw(amount)`: Deducts the specified amount from the balance, ensuring that the balance does not become negative.
     - `transfer(amount, target_account)`: Transfers the specified amount from this account to another `target_account`.
     - `__str__()`: Returns a string summarising the account details, including the owner's name, account number, and current balance.

2. **SavingsAccount (Inherits from Account)**:
   - Inherits the properties and methods of `Account`.
   - Additional Method:
     - `apply_interest(rate)`: Increases the balance by a given percentage (`rate`). The rate must be a positive value.

3. **CurrentAccount (Inherits from Account)**:
   - Inherits the properties and methods of `Account`.
   - Overdraft Support:
     - This account type allows overdrafts (negative balances) up to a predefined limit.
   - Attribute:
     - `overdraft_limit`: The maximum overdraft allowed.
   - Overridden Method:
     - `withdraw(amount)`: Withdrawals are allowed up to the overdraft limit.

4. **Bank Class**:
   - Attributes:
     - `accounts`: A collection of accounts (could be a list or dictionary) managed by the bank.
   - Methods:
     - `add_account(account)`: Adds an account to the bank’s account list.
     - `get_account(account_number)`: Returns an account object using the account number.
     - `total_balance()`: Calculates the total balance across all accounts in the bank.
     - `remove_account(account_number)`: Removes an account from the bank’s account list.
     - `get_all_accounts()`: Returns a summary of all accounts in the bank.

#### Additional Requirements:
- **Account Validation**: Ensure that account numbers are unique.
- **Edge Case Handling**:
  - Ensure negative deposits or withdrawals are not allowed unless supported (e.g., overdrafts).
  - Disallow transfers that exceed the available balance (in the case of savings accounts).
  - Ensure transfers between accounts work correctly and balances are updated accordingly.
  
- **TDD Approach**: 
  - For each class and method, tests should be written first, covering both positive scenarios (e.g., successful deposits) and edge cases (e.g., withdrawing more than available balance). 
  - All tests should pass before moving to the next feature.
  
#### Example Scenarios to Test:
1. Create an account, deposit money, and check the balance.
2. Withdraw an amount and ensure the balance is updated correctly.
3. Attempt to withdraw more than the available balance for a savings account and ensure an error is raised.
4. Transfer money between two accounts and verify that the balances of both accounts are updated correctly.
5. Apply interest to a savings account and verify that the balance increases.
6. Ensure a current account can go into overdraft, but not beyond the specified limit.
7. Calculate the total balance for all accounts in the bank.
8. Ensure account removal works properly.

#### Optional Extensions:
- **Account Types**: Implement additional account types such as joint accounts or business accounts.
- **Transaction History**: Record every deposit, withdrawal, and transfer in a transaction history.
- **User Interface**: Create a command-line interface (CLI) or a simple web interface for users to interact with the bank system.
- **Security Features**: Add basic password protection or account PIN functionality.

#### Deliverables:
- Full implementation of the classes with all specified methods and attributes.
- A complete test suite that thoroughly tests all the methods using TDD principles.
- Detailed documentation explaining the code and how to run the tests.

---

This brief provides a clear structure to guide your development, with room for additional features if you want to expand the project. It covers class design, interaction between objects, and thorough testing, making it an excellent way to practise OOP and TDD.