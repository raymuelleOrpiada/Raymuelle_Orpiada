class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected
        self.__balance = balance  # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw: {amount}")
        else:
            print("Amount must be positive and less than or equal to the current balance.")

    def display_account_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Current Balance: {self.__balance}")

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
            print(f"Balance set to: {balance}")
        else:
            print("Balance cannot be negative.")
account = BankAccount("123456789", 1000.0)
account.deposit(1000)
account.withdraw(100)
account.set_balance(-100)
account.display_account_info()