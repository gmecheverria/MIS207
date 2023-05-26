import PE30
my_cup = PE30.Cup(16)
your_cup = PE30.Cup(32)
print(f"To start, my cup has {my_cup.getAmount()} ounces and your cup has {your_cup.getAmount()} ounces")

my_cup.fill()
your_cup.fill()
print(f"After filling, my cup has {my_cup.getAmount()} ounces and your cup has {your_cup.getAmount()} ounces")

print(f"Taking a drink - I get {my_cup.drink(3)} ounces from my cup and {your_cup.drink(3)} ounces from your cup.")

my_cup.sip()
your_cup.sip()
print(f"Taking a sip - I get {my_cup.sip()} ounces from my cup and {your_cup.sip()} ounces from your cup.")

my_cup.gulp()
your_cup.gulp()
print(f"Taking a gulp - I get {my_cup.gulp()} ounces from my cup and {your_cup.gulp()} ounces from your cup.")


print(f"What's left in my cup is {my_cup.getAmount()} ounces and in your cup {your_cup.getAmount()} ounces.")