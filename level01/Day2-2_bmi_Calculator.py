#BMI Calculator

height = input("Enter your height im  m : ")
weight = input("Enter your weight in kg : ")
result = int(weight) / float(height) ** 2
final_result = round(result,2)
print (f"Your BMI is {final_result}")