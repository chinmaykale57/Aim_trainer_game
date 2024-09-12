def calculator(a, b, operation):
    if operation == "+":
        return a+b
    if operation == "-":
        return a-b
    if operation == "/":
        if b == 0:
            return "Error division by zero"
        return a/b
    if operation == "*":
        return a*b
    if operation == '^':
        return a**b    
    else:
        return "Error: Invalid operation"

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Please enter the operation (+, -, *, /, ^): ")
result = calculator(a, b, operation)
print("the answer is: ", result)
