import stdiomask
import math
import getpass

def add_num(a, b):
    return a + b

def sub_num(a, b):
    return a - b

def div_num(a, b):
    if b == 0:
        print("Error Division by zero")
    else:
        return a / b

def mul_num(a, b):
    return a * b

def expo(a, b):
    return pow(a, b)

while True:

    print("----- CALCULATOR 3000 ----- \n-------- WELCOME! --------")
    name = input("Enter your name: ")
    password = stdiomask.getpass("Enter your password: ", mask ="#")

    if password == "admin":
        print("\nWelcome", name, "\nSelect below the number of operator you want to use.")
        break
    else:
        print("Wrong password try again!")

while True:
    valid_operators = ["1", "2", "3", "4","5"]
    print("\n1.add\n2.subtract\n3.Divide\n4.Multiply\n5.Exponential")
    operand = input("select operator: ")
    if operand in valid_operators:
        print("nice, now input 2 numbers")
        break
    else:
        print("OOps!,",operand,  "is not in the choices")

while True:
        num1 = (input("Enter your first Number: "))
        num2 = (input("Enter your second number: "))
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            break
        else:
            print("must only input numbers")

if operand == "1":
    result_1 = add_num(num1,num2)
    print(num1, " +  ", num2, " = ", result_1)
elif operand == "2":
    result_1 = sub_num(num1, num2)
    print(num1, " -  ", num2, " = ", result_1)
elif operand == "3":
    result_1 = div_num(num1, num2)
    print(num1, " /  ", num2, " = ", result_1)
elif operand == "4":
    result_1 = mul_num(num1, num2)
    print(num1, " *  ", num2, " = ", result_1)
elif operand == "5":
    result_1 = expo(num1, num2)
    print(num1, "raise to the power of ", num2, " = ", result_1 )
else: 
    print("wrong input")

while True:
    another_go = input("Do you want to calculate again? (y/n): ")
    if another_go.lower() == "y":
        while True:
            operand = input("select operator: ")
            if operand in valid_operators:
                print("nice, now input 2 numbers")
                break
            else:
                    print("OOps!,",operand,  "is not in the choices")

        while True:
            num1 = (input("Enter your first Number: "))
            num2 = (input("Enter your second number: "))
            if num1.isdigit() and num2.isdigit():
                num1 = int(num1)
                num2 = int(num2)
                break
            else:
                print("must only input numbers")

        if operand == "1":
            result_1 = add_num(num1,num2)
            print(um1, " +  ", num2, " = ", result_1)
        elif operand == "2":
            result_1 = sub_num(num1, num2)
            print(num1, " -  ", num2, " = ", result_1)
        elif operand == "3":
            result_1 = div_num(num1, num2)
            print(num1, " /  ", num2, " = ", result_1)
        elif operand == "4":
            result_1 = mul_num(num1, num2)
            print(num1, " *  ", num2, " = ", result_1)
        elif operand == "5":
            result_1 = expo(num1, num2)
            print(num1, "raise to the power of ", num2, " = ", result_1 )
        else:
            print("wrong input")
    elif another_go == "n":
        print("thank u  for using calculator 3000!")
        exit()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")













