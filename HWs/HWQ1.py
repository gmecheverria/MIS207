#
# prints the valance of an account after the first, second, third, and fourth year.
#
initialBalance = 250  # initial balance
interest = 0.07  # 7 percent interest per year

# calculates the first year balance
balance1 = initialBalance + (initialBalance * interest)
print("First Year:", "$", balance1)

# calculates the second year balance
balance2 = balance1 + (balance1 * interest)
print("Second Year:", "$", round(balance2, 2))

# calculates the third year balance
balance3 = balance2 + (balance2 * interest)
print("Third Year:", "$", round(balance3, 2))

# calculates the fourth year balance
balance4 = balance3 + (balance3 * interest)
print("Fourth Year:", "$", round(balance4, 2))
