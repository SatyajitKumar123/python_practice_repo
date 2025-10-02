class BankAccount:
    def __init__(self, account_holder, balance = 0):
        # Public attribute - accessible from outside
        self.account_holder = account_holder

        # Private attribute (indicated by _) - should not be accessed directly
        self._account_number = id(self)

        # "Protected" attribute (indicated by __) - name mangling makes it harder to access
        self.__balance = balance

    # Public method - interface for external use
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Public method to safely access private data
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount!")

    # Public method to safely modify private data with validation
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative!")

# Using the encapsulated class     
account = BankAccount("Satya", 1000)

# This works - using public interface
print(f"Account holder: {account.account_holder}")
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.get_balance()}")

