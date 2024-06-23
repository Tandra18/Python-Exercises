# Display numbers divisible by 5 from a list


list = []
while True:
   elements = int(input("Enter elements :"))
   if elements == -1:
       print("\nThe given list is :", list)
       break
   list.append(elements)
   print(list)

div_5_array = []
for i in list:
    if i % 5 == 0:
        div_5_array.append(i)

print("The elements divisible by 5 is :",div_5_array)
