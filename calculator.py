print("Cour Calculator")

user_input_1 = input("Enter first Number: ")
user_input_2 = input("Enter Second Number: ")
operator = input("Enter Prefered operator: ")


# error handling

try:
    num1 = int(user_input_1)
    num2 = int(user_input_2)
except ValueError:
    print("Invalid Input. try again!!")
    exit


def calculate(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
        print(f"Answer: {resdsa.py
        ult}")
    elif operator == '-':
        result = num1 - num2
        print(f"Answer: {result}")
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print(f"Answer: {result}")        
    elif operator == '*':
        result = num1 * num2
        print(f"Answer: {result}")
    else:
        print("Invalid")


calculate(num1, num2, operator)
