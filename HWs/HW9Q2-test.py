from HW9_Q2 import BankAccount

b1 = BankAccount(200)
print(b1)
b1.deposit(500)
print(b1.get_balance())

b2 = BankAccount(500)
print(b2)
b2.withdraw(300)
print(b2.get_balance())

b3 = BankAccount(50)
print(b3)
b3.withdraw(100)
print(b3.get_balance())


