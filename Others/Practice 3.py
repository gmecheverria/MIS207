def print_list_formatting(my_dict):
    for data in my_dict:
        print(f'{data}: {my_dict[data] * "*"}')

def word_formatting(lines):
    my_dict = {}
    words = lines.split()
    for word in words:
        word = word.lower()
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
        # my_dict[word] = my_dict.get(word, 0) + 1
    return my_dict

infile = open("input-1.txt", "r")
lines = infile.read()
infile.close()
print_list_formatting(word_formatting(lines))
