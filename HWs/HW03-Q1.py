##
# Prompts for the day and month of the user’s birthday and then prints a horoscope
##

# Title
print("Determines your Horoscope")

# Gets the users input
print("Enter your birthday.")
mouth = int(input("Mouth:"))
day = int(input("Day:"))

# Prints the horoscope based on the users birthday
if mouth == 1 and day >= 20 or mouth == 2 and day <= 18:
    print("Aquarius are progressive, original, independent, and humanitarian")
elif mouth == 2 and day >= 19 or mouth == 3 and day <= 20:
    print("Pisces are compassionate, artistic, intuitive, and gentle")
elif mouth == 3 and day >= 21 or mouth == 4 and day <= 19:
    print("Aries are courageous, determined, confident, and enthusiastic")
elif mouth == 4 and day >= 20 or mouth == 5 and day <= 20:
    print("Taurus are reliable, patient, practical, and devoted")
elif mouth == 5 and day >= 21 or mouth == 6 and day <= 20:
    print("Gemini are gentle, affectionate, curious, and adaptable")
elif mouth == 6 and day >= 21 or mouth == 7 and day <= 22:
    print("Cancer are tenacious, highly imaginative, loyal, and sympathetic")
elif mouth == 7 and day >= 23 or mouth == 8 and day <= 22:
    print("Leo are creative, passionate, generous, and warm-hearted")
elif mouth == 8 and day >= 23 or mouth == 9 and day <= 22:
    print("Virgo are loyal, analytical, kind, and hardworking")
elif mouth == 9 and day >= 23 or mouth == 10 and day <= 22:
    print("Libra are cooperative,diplomatic, gracious, and fair-minded")
elif mouth == 10 and day >= 23 or mouth == 11 and day <= 21:
    print("Scorpio are resourceful, powerful, brave, and passionate")
elif mouth == 11 and day >= 22 or mouth == 12 and day <= 21:
    print("Sagittarius are generous, idealistic, and great sense of humor")
else:
    print("Capricorn are responsible, disciplined, self-control, and good managers")
