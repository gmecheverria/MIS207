#
# Write and test a function that translates a telephone number written in letters to an actual phone number.
# Test your function by calling the function with three different inputs.
# Assumptions: You can assume that all given numbers (in letters)
# will consist of only the letters in the number (no numbers, or extra characters).
#

def phone_number(word_number):
    return_str = ""
    for letter in word_number:
        if letter in 'ABC':
            return_str += str(2)
        elif letter in 'DEF':
            return_str += str(3)
        elif letter in 'GHI':
            return_str += str(4)
        elif letter in 'JKL':
            return_str += str(5)
        elif letter in 'MNO':
            return_str += str(6)
        elif letter in 'PQRS':
            return_str += str(7)
        elif letter in 'TUV':
            return_str += str(8)
        elif letter in 'WXYZ':
            return_str += str(9)
        else:
            return_str += ""
    return return_str



# Wrong/long way of doing it


def main():
    print("Your phone number is", phone_number("A,D,G,J,M,P,T,W,T,W"))
    print("Your phone number is", phone_number("z,q,a,g,k,m,p,w,w,y"))
    print("Your phone number is", phone_number("P,n,I,s,L,m,n,o,h,G"))


def phone_number(letter):
    letter = letter.split(",")
    number1 = gets_number(letter[0])
    number2 = gets_number(letter[1])
    number3 = gets_number(letter[2])
    number4 = gets_number(letter[3])
    number5 = gets_number(letter[4])
    number6 = gets_number(letter[5])
    number7 = gets_number(letter[6])
    number8 = gets_number(letter[7])
    number9 = gets_number(letter[8])
    number10 = gets_number(letter[9])

    return "(" + number1 + number2 + number3 + ")" + number4 + number5 + number6 + "-" \
           + number7 + number8 + number9 + number10


def gets_number(letter):
    if letter.upper() == "A" or letter.upper() == "B" or letter.upper() == "C":
        digit = "2"
    if letter.upper() == "D" or letter.upper() == "E" or letter.upper() == "F":
        digit = "3"
    if letter.upper() == "G" or letter.upper() == "H" or letter.upper() == "I":
        digit = "4"
    if letter.upper() == "J" or letter.upper() == "K" or letter.upper() == "L":
        digit = "5"
    if letter.upper() == "M" or letter.upper() == "N" or letter.upper() == "O":
        digit = "6"
    if letter.upper() == "P" or letter.upper() == "Q" or letter.upper() == "R" or letter.upper() == "S":
        digit = "7"
    if letter.upper() == "T" or letter.upper() == "U" or letter.upper() == "V":
        digit = "8"
    if letter.upper() == "W" or letter.upper() == "X" or letter.upper() == "Y" or letter.upper() == "Z":
        digit = "9"

    return digit


main()
