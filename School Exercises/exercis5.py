# A = [3, 8, 1, 2, 5]
# smallest = min(A)
# largest = max(A)
#
# print("List : ",A)
# print("Smallest : ",smallest)
# print("Largest : ",largest)


def finding(numbers):
    smallest = float('inf')
    largest = float('-inf')

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return largest, smallest

A = [3, 8, 1, 2, 5]
largest,smallest = finding(A)
print("The list is : ",A)
print("The largest number is : ",largest)
print("The smallest number is : ",smallest)