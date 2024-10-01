#sum of all even numbers between 1 and 100
sum_of_even_numbers = 0

for num in range(1,101):
    if num % 2 == 0:
        sum_of_even_numbers += num

print("The sum of all even numbers between 1 and 100"
      " is :",sum_of_even_numbers)