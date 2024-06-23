# Write a program to check if the given number is a palindrome number.
#
# A palindrome number is a number that is the same after reverse.
# For example, 545, is the palindrome numbers

import math
def palindrome(number):
    print("Original number :",number)
    original_num = number

    reverse_num = 0
    while number > 0 :
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    if original_num == reverse_num:
        print("The number is palindrome.")

    else:
        print("The number is not palindrome.")

palindrome(int(input("Enter a number to test :")))
