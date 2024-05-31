#Find the factorial of a given number

factorial = 1
n = int(input("Enter a number :"))
if n < 0 :
    print("Cannot find factorial of negative number.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1,n+1):
        factorial = factorial * i
    print(factorial)