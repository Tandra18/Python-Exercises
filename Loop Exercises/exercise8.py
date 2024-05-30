#Print list in reverse order using a loop

# first solution
# list = [10, 20, 30, 40, 50, 60]
# n = list.reverse()
# for i in list:
#     print(i)

list = [10, 20, 30, 40, 50, 60]
size = len(list) - 1
for i in range(size, -1, -1):
    print(list[i])
