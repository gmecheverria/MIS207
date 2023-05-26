def get_number(lines):
    total = 0
    for line in lines:
        line = lines.split()
        for i in line:
            try:
                total += int(i)
            except ValueError:
                i = 0
        break
    print(total)


infile = open("input.txt", "r")
lines = infile.read()
infile.close()
get_number(lines)

