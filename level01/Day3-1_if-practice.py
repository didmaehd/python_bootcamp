#odd and even number
number = int(input("Which number you want to choose "))
if number % 2 == 0:
    print("This is a even number.")
else :
    print("This is an odd number.")


height = int(input("How tall are you? "))
if height >= 120 :
    age = int(input("How old are you? "))
    if age < 12:
        print("Please pay $5")
    elif age >= 12 and age <= 18:
        print("Please pay $7")
    elif age > 18:
        print("Please pay $12")
else :
    print("Sorry you so too short to ride this")
    