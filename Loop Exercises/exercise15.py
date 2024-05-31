#Calculate the cube of all numbers from 1 to a given number

number = int(input("Enter a number :"))
for i in range(1, number+1):
    cube = i * i * i
    print("The current number is :",i,"\nIts cube is : ", cube)