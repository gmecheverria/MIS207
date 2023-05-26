##
#  This program prints a table of medal winner counts with row totals.
#

# Create a list of country names.
countries = [ "Canada",
              "Italy",
              "Germany",
              "Japan",
              "Kazakhstan",
              "Russia",
              "South Korea",
              "United States" ]
              
# Create a table of medal counts.              
counts = [ 
           [0, 3, 0],
           [0, 0, 1],
           [0, 0, 1],
           [11, 0, 0],
           [0, 0, 1],
           [3, 1, 1],
           [0, 1, 0],
           [1, 0, 1]
    ]

print(f"{' ':<20}{'Gold':^7}{'Silver':^7}{'Bronze':^7}")
count = 0
for row in counts:
    print(f"{countries[count]:<20}", end="")
    count += 1
    for col in row:
        print(f"{col:^7}", end="")
    print()


