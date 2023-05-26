#
# Write your program so that it displays this data as a table.
#

data = {
    "00111": {
        "description": "Hockey Stick",
        "price": 12.23,
        "quantity": 23
    },
    "00223": {
        "description": "Baseball",
        "price": 8.78,
        "quantity": 32
    },
    "00451": {
        "description": "Basketball",
        "price": 29.63,
        "quantity": 19
    },
    "04022": {
        "description": "Puck",
        "price": 2.87,
        "quantity": 22
    }
}
print(f'{"Key":10}{"Description":13}{"Price":>10}{"Quantity":>10}')
print("-" * (10+13+10+10))
for record in data:
    print(f"{record:10}{data[record]['description']:13}{data[record]['price']:10}{data[record]['quantity']:10}")


