#Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


rows = 5
for x in range(1, rows+1, 1):
    for y in range(1,x+1):
        print(y, end=" ")
    print(" ")

