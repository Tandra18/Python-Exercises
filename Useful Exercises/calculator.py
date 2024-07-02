
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

print("Choose operation :")
print("1 for add,\n2 for substract,\n3 for multiply,\n4 for division")

choice = int(input())
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))

if choice == 1 :
    print("The addition is : ",add(num1,num2))
elif choice == 2 :
    print("The substraction is :",subtract(num1,num2))
elif choice == 3 :
    print("The multiplication is :",multiply(num1,num2))
elif choice == 4:
    print("The multiplication is :",divide(num1,num2))
else:
    print("Invalid number !4")
