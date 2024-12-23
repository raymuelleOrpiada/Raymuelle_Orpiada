class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
        else:
            print("Invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Error: Balance cannot be negative.")

    def __display_balance(self):
        print(f"Current Balance: {self.__balance}")


my_account = BankAccount("123456789", 1000.00)
my_account.deposit(500.00)
my_account.withdraw(200.00)
my_account.set_balance(-500.00) 
my_account.display_account_info()
my_account.__display_balance() 