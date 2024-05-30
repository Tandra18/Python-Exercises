#Write a program to print multiplication table of a given number

n = int(input("Please enter a number :"))
for i in range(1, 11, 1):
    product = n * i
    print(product)