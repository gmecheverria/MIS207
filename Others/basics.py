# create a list
a_list = [1, 2, 3, "alpha"]

# display contents of list (good when formatting doesn't
# matter)
print(a_list)

# concatenate two lists
b_list = ['beta', 4]
c_list = a_list + b_list
print(c_list)

# add items to a list
## method 1 - append
c_list.append('dog')
print(c_list)

## method 2 - insert
c_list.insert(1, 'cat')
print(c_list)

# c_list.insert('cat') # this would generate an error - you
# need two arguments
print(c_list)

## method 3 - concatenate
x = 123
y = 234
z = 345
c_list = c_list + [x]  # note: shorter form of this is c_list += [x]
c_list = c_list + [y, z]
c_list += [x]
c_list += [y, z]
print(c_list)

# remove an item from a list
## method 1 - pop
c_list.pop()  # pops the last item from list
print(c_list.pop())

c_list.pop(2)  # pops item at index location from list

## method 2 - remove
c_list.remove('cat')  # removes the given value from a list
print(c_list)

# c_list.remove('cat')  # this generates an error, because 'cat' is not found in the list
# print(c_list)

if 'cat' in c_list:
    c_list.remove('cat')
else:
    print("cat wasn't found in the list")

## method 3 - delete
del c_list[1] # this is like pop, but doesn't return a value like pope
print(c_list.pop(0)) # notice that pop returns the item that was removed

# sort list
# c_list.sort()
# print(c_list)  # generates an error if mixing types

d_list = [2, 4, 1, 7, 5, 19, 0, -1]
d_list.sort()  # ok, since all elements can be < or > than each other
print(d_list)

e_list = ['cadabra', 'abbra', 'hello']
e_list.sort() # ok, since all elements can be < or > than each other
print(e_list)

# selecting items from a list
## select one item
print(c_list[0])

## select the last item
### method 1 - using len
print(c_list[len(c_list)-1])
### method 2 - negative indexing
print(c_list[-1])

## select two items
print(c_list[0:2])

## select a range of items
print(c_list[0:5])

## select from start of list
print(c_list[:2])

print([c_list[0], c_list[-1]])

## select until end of list
print(c_list[2:])

## use increment to select every second item
print(c_list[::2])

## use increment (negative amount) to reverse a list
print(c_list[::-1])

# copying list
## method 1 -- list function
list_copy = list(c_list)

## method 2 -- slice entire list
list_copy2 = c_list[:]

# randomly select items from a list
import random
print(random.choice(c_list))
print(random.choice(c_list))
print(random.choice(c_list))

# patterns - loop through entire list
for item in c_list:
    print(item)

# patterns - create empty list, and add items to list
some_list = []
print("Please enter 3 numbers: ")
for i in range(1, 4):
    num = float(input(f"Enter #{i}: "))
    some_list += [num]
print('The numbers you entered were...')
print(some_list)

# some useful list functions
z_list = [1, 2, 3, 4]
print(max(z_list))
print(min(z_list))
print(sum(z_list))
print(sum(z_list)/len(z_list))

