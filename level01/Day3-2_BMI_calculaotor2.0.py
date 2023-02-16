height = input("Enter your height im  m : ")
weight = input("Enter your weight in kg : ")
result = int(weight) / float(height) ** 2
final_result = round(result,2)

if final_result < 18.5:
    print(f"Your BMI is {final_result}. You are underweight")
elif final_result >= 18.5 and final_result < 25:
    print(f"Your BMI is {final_result}. You are nomal weight")
elif final_result >= 25 and final_result < 30:
    print(f"Your BMI is {final_result}. You are overweight")
elif final_result >= 30 and final_result <= 35:
    print(f"Your BMI is {final_result}. You are obese")
elif final_result >35:
    print(f"Your BMI is {final_result}. You are clinically obese")

