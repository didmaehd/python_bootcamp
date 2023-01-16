#pizza
bill = 0
size = input("What size pizza do you want? S, M, L : ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
add_pepperoni = input("Do you wnat add pepperoni? Y, N : ")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
add_cheese = input("Do you wnat add extra cheese? Y, N : ")
if add_cheese == "Y":
    bill += 1
    print(f"Your pay is ${bill}")
else:
    print(f"Your pay is ${bill}")
