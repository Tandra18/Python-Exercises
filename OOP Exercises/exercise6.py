# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

str = input("Enter a string : ")
print("The string is [",str,"]")
size = len(str)

print("Printing only the even index of chars")
for i in range(0,size -1,2):
    print("index [",i,"]",str[i])

#different approach

# word = input("Enter a string :")
# print("The string is : [",word,"]")
# x = list(word)
# for i in x[0::3]:
#     print(i)