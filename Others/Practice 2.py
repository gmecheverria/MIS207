def rectangle(rows, cols):
    for row in range(rows):
        for col in range(cols):
            if row == 0 or row == rows-1 or col == 0 or col == cols-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

rectangle(10, 5)
print()

