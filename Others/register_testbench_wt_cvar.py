from register_wth_cvar import CashRegister

print("total1", CashRegister.total_sales)

register_01 = CashRegister()
register_02 = CashRegister(100)

print("total2", CashRegister.total_sales)
print(register_01)
print(register_02)

register_01.add_item(9.95, 5)

print("total3", CashRegister.total_sales)
print(register_01)
print(register_02)

register_02.add_item(23.95, 1)
register_02.add_item(15.95, 3)

print("total4", CashRegister.total_sales)
print(register_01)
print(register_02)

register_01.clear()
register_02.clear()

print("total5", CashRegister.total_sales)
print(register_01)
print(register_02)



