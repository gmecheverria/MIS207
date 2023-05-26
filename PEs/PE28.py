#
# Write a program that uses this dictionary (copy it into your program)
# and displays the medals in a nicely formatted table
#

medals = {
    'Canada': {"Gold": 3, "Sliver": 3, "Bronze": 4},
    'China': {"Gold": 13, "Sliver": 14, "Bronze": 18},
    'United States': {"Gold": 23, "Sliver": 28, "Bronze": 32}
}

print(f"{' ':<20}{'Gold':^7}{'Silver':^7}{'Bronze':^7}")

for key in medals:
    print(f"{key}{medals[key]['Gold']:^13} {medals[key]['Sliver']:^13} {medals[key]['Bronze']:^13}")
