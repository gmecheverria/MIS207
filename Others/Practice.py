def list_square(list):
    ret_list = []
    for new_row in list:
        row = []
        for col in new_row:
            row.append(col**2)
        ret_list.append(row)
    return ret_list

def print_2d_list(list):
    for row in list:
        for col in row:
            print(f'{col:^7}', end="")
        print()
    return

print_2d_list(list_square([ [1,2,3,4] ]))
print()
print_2d_list(list_square([ [1,2,3], [5,6,7], [4,8,9] ]))
print()