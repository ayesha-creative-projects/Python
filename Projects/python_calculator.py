operator = input("Enter any operator(+ - * /): ")

# Check if the operator is valid FIRST
if operator == "+":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1 + num2
    print(round(result, 3))

elif operator == "-":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1 - num2
    print(round(result, 3))

elif operator == "*":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1 * num2
    print(round(result, 3))

elif operator == "/":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1 / num2
    print(round(result, 3))

else:
    # This runs immediately if the first input was wrong
    print("Choose given operators")