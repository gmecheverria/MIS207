#
# Create a class called BankAccount.
# Objects of the BankAccount class should hold a current balance
# and account number and allow you to deposit, withdraw, get_balance, and get_account_number.
# Objects of the BankAccount class should be printable, and when printed, display the account number and current balance
# Each bank account should generate a unique Account Number when created.
# You will implement the unique account number generation by using a class variable
# that holds the count of objects that have been created by the class.
# As an object is created from the class, this class variable is incremented,
# and this incremented number is used for the account number of the current object.
#

class BankAccount:
    count = 0

    def __init__(self, balance):
        self._balance = balance
        BankAccount.count += 1
        self._account_num = self.count

    def __str__(self):
        return f'Account Number: {self._account_num} \nCurrent Balance: {self._balance}'

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance < amount:
            print("insufficient funds")
            return self._balance
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_num
