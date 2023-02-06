import os
import Day10_art
print (Day10_art.logo)

calc = True
stored_number = 0

def addition(f_number,s_number):
    return f_number + s_number
def subtraction(f_number,s_number):
    return f_number - s_number
def multiplication(f_number,s_number):
    return f_number * s_number
def division(f_number,s_number):
    return f_number / s_number

while calc:
    f_number = int(input("What's the first number? : "))
    operation = input("""
+
-
*
/
Pick an operation : """)
    s_number = int(input("What's the second number? : "))



    if operation == "+" :
        result = (addition(f_number,s_number))
    if operation == "-" :
        result = (subtraction(f_number,s_number))
    if operation == "*" :
        result = (multiplication(f_number,s_number))
    if operation == "/" :
        result = (division(f_number,s_number))
    print(f"{f_number} {operation} {s_number} = {result}")
    stored_number = result

#결과값을 기준으로 추가 계산을 할 것인지, 혹은 새로룬 계산을 할 것인지
    retry = input(f"Type 'y' to continue calculatiing with {stored_number}, or type 'n' to start a new calculation : ")
    if retry == "y":
        calc = False
        recal = True
        while recal :
            operation = input("Pick an operation : ")
            s_number = int(input("What's the second number? : "))
            if operation == "+" :
                result = (addition(stored_number,s_number))
            if operation == "-" :
                result = (subtraction(stored_number,s_number))
            if operation == "*" :
                result = (multiplication(stored_number,s_number))
            if operation == "/" :
                result = (division(stored_number,s_number))
            print(f"{stored_number} {operation} {s_number} = {result}")
            stored_number = result
            retry = input(f"Type 'y' to continue calculatiing with {stored_number}, or type 'n' to start a new calculation : ")
            if retry == "y":
                recal = True
            elif retry == "n":
                recal = False
                calc = True
                os.system('cls')
    elif retry == "n":
        calc = True
        os.system('cls')







