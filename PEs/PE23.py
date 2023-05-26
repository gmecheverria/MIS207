#
#  Write and test a function that accepts a 2d list of numbers, and returns
#  the average, number of rows, and number of columns...
#  For instance sum_2d([[1,2],[2,3]]) should return (2,2,2)
#  NOTE: You can return multiple values by returning a tuple#
#  i.e. return (num1, num2, num3)
#

def sum_2d(list):
    row_count = len(list)
    col_count = len(list[0])
    total = 0
    for row in list:
        total += sum(row)
    return int(total/(row_count*col_count)), row_count, col_count

print(sum_2d([[1,2],[2,3]]))
