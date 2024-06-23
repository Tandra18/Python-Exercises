# Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.

pre_num = 0
for i in range(1,10):
    sum = pre_num + i
    print("Current number", i, "Previous number ", pre_num, "Sum :", sum)
    pre_num = i
