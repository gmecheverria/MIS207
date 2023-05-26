#
# Your objective is to create and test a function called create_random_table
# that accepts a number of rows, a number of columns, a min value,
# and a max value and returns a new table with these dimensions
# and with a random integer in each location (selected from the range between min and max).
#

import random

def display_table(table, col_width):
    for row in table:
        for col in row:
            print(f'{col:{col_width}}', end="")
        print()

def create_random_table(row_count, col_count, min_value, max_value):
    ret_list = []
    for row in range(row_count):
        row = []
        for col in range(col_count):
            row.append(random.randint(min_value, max_value))
        ret_list.append(row)
    return ret_list

# tests
display_table(create_random_table(10,10, 0, 9), 3)
print()
display_table(create_random_table(5,10, 0, 20), 3)
print()
display_table(create_random_table(3,4, 1000, 2000), 6)


