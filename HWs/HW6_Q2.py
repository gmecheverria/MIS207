#
# Write and test a function that accepts a table (2-dimensional list)
# and prints the contents of the table in a grid/table-like format.
# Each column should be 10 characters wide and the contents of each cell should be centered.
#

def table_format(list):
    for row in list:
        for col in row:
            print(f"{col:^10}", end="")
        print()


# tests the function
table_format([[1, 2, 3], [4, 5, 6]])
table_format([['house', 'dog'], ['cottage', 'cat']])
