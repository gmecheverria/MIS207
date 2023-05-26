from register_original import CashRegister

register_01 = CashRegister()

register_02 = CashRegister(100)

print(register_01)
print(register_02)

register_01.add_item(9.95, 5)

print(register_01)
print(register_02)

register_02.add_item(23.95, 1)
register_02.add_item(15.95, 3)

print(register_01)
print(register_02)

register_01.clear()
register_02.clear()

print(register_01)
print(register_02)



