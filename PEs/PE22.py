#
# Write and test a function called list_filter that accepts a list of numbers,
# and a minimum value and returns a new list with all elements of the
# original list that are larger than the given minimum value.
# For instance, if I call it as follows list_filter([1,2,3,4], 2) it would return a list containing [3,4]

def list_filter(list_num, min_num):
    new_list = list_num[:]
    for num in new_list:
        if num <= min_num:
            new_list.pop(num)
    print(new_list)


list_filter([1,2,3,4], 2)

