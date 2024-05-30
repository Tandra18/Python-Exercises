#Write a program to display all prime numbers within a range

start = int(input("Enter a start number :"))
end = int(input("Enter a end number :"))
for num in range(start, end + 1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)