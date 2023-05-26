#
# Read this file, and calculate the total population of all the countries list in this file.
#

in_file = open('countries.txt', 'r', encoding='utf-8')

txt = in_file.read()
lines = txt.split('\n')

total = 0
for line in lines:
    if ':' in line:
        countries, price = line.split(':')
        total += int(price)

print(f'Total population is {total:,.2f}')
in_file.close()
