#
#  Create and test a function that accepts a list of digits
#  and returns a new list containing the word for each of the digits found.
#


def digit_list_to_str(list):
    ret_list = []
    for digit in list:
        if digit == 0:
            ret_list.append('zero')
        elif digit == 1:
            ret_list.append('one')
        elif digit == 2:
            ret_list.append('two')
        elif digit == 3:
            ret_list.append('three')
        elif digit == 4:
            ret_list.append('four')
        elif digit == 5:
            ret_list.append('five')
        elif digit == 6:
            ret_list.append('six')
        elif digit == 7:
            ret_list.append('seven')
        elif digit == 8:
            ret_list.append('eight')
        elif digit == 9:
            ret_list.append('nine')
        else:
            ret_list.append('INVALID VALUE')
    return ret_list



print(digit_list_to_str([2, 2, 3, 1, 8, 9]))

print(digit_list_to_str([9, 0, 6, 3, 7, 8]))
