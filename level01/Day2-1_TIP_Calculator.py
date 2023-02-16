#TEST01
number = input("Type a two digit number: ")
result = int(number[0]) + int(number[1])
print(result)




# Welcome message
print ("Welcome to the tip calculator")
# input values
total_bill = input("What was the total bill? $ ")
split_num = input("How many people to split the bill? ")
tip_rate = input("What percentage tip would you like to give? 10, 12, or 15? ")
# calculate tip
fix_tip = int(total_bill) * int(tip_rate) * 0.01
#calculate total price that was added tip
total_price = int(total_bill) + int(fix_tip)
#calculate cost per head
result = int(total_price) / int(split_num)
print (f"Each person should pay: ${result}")


