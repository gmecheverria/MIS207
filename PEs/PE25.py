in_file = open('waldo.txt', 'r')

count = 0
for line in in_file:
    word = line.split()
    for word in word:
        if "waldo" in word.lower():
            count += 1

print(count)
in_file.close()

