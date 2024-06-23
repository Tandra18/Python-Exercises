# Given two list of numbers, write a program to create a
# new list such that the new list should contain odd numbers from
# the first list and even numbers from the second list.

list_1 = []
while True:
    elements = int(input("Enter elements for list 1 : "))
    if elements == -1:
        print("The list 1 is : ", list_1)
        break
    list_1.append(elements)
    print("The list 1 is : ",list_1)

list_2 = []
while True:
    elements = int(input("Enter elements for list 2 : "))
    if elements == -1:
        print("The list 2 is : ",list_2)
        break
    list_2.append(elements)
    print("The list 2 is : ",list_2)

def merge_list(list_1,list_2):
    new_list = []

    for num in list_1:
        if num % 2 != 0:
            new_list.append(num)

    for num in list_2:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
print("The new list is : ",merge_list(list_1,list_2))
