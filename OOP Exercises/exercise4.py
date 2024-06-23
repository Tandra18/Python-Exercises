num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))
product = num1 * num2
sum = num1 + num2

if (product <= 1000):
    print("The result is ", product)
else:
    print("The result is ", sum)


# different approach
# def mul_or_sum(num1,num2):
#     product = num1 * num2
#
#     if product <= 1000:
#         return product
#     else:
#         return num1 + num2
#
# result = mul_or_sum(int(input("Enter num1 :")),int(input("Enter num 2 :")))
# print("The result is " , result)



