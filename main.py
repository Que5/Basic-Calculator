
print("Welcome to the calculator!")

num1_string = input("First number:")
num1 = int(num1_string)
operation = input("To add put +, to subtract put -, to divide put /, to multiply put *!")
num2_string = input("Second number:")
num2 = int(num2_string)

def calculations(num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "/":
        return num1 / num2
    elif operation == "*":
        return num1 * num2
    else:
        return "Your choice is invalid"
        
total = calculations(num1,num2)
total_final = int(total)
print("Total is" ,total_final,"!")
print("Thank you")
    





