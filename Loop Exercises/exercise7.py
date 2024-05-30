#Write a program to use for loop to print the following reverse number pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


rows = 4
# k = 5
k = int(input("Enter a number :"))
for i in range(0,rows+1):
    for j in range(k-i, 0 , -1):
        print(j, end=" ")
    print()