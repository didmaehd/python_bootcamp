height = int(input("Hoe tall are you? : "))
bill = 0
if height > 120:
    age = int(input("How old are you? : "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
    else : 
        bill = 12
    photo = input("Do you want to take a photo? Y or N : ")
    if photo == "Y":
        bill += 3
        print(f"Your pay is ${bill}")
    else :
        print(f"Your pay is ${bill}")
else :
    print("You are too shoty to ride this. ")
