# Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

def first_last_num(numberlist):

    first_num = numberlist[0]
    last_num = numberlist[-1]

    if first_num == last_num:
        return True
    else:
        return False

list_1 =[]
while True:
    print("Enter element for list 1:")
    elements = input()
    if elements == "quit":
        print("The list 1 is :",list_1)
        break
    list_1.append(elements)
    print("The list 1 is :",list_1)

print(first_last_num(list_1))

list_2 = []
while True:
    elements = input("Enter element for list 2 :")
    if elements == "quit":
        print("The list 2 is :",list_2)
        break
    list_2.append(elements)
    print("The list 2 is :",list_2)

print(first_last_num(list_2))