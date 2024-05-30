# Display numbers that can be divisible by 5 from a list using loop
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

numbers = [12, 50, 75, 150, 140, 180, 145, 525]
for i in numbers:
    if i > 150:
        continue
    elif i > 500:
        break
    elif i % 5 == 0:
        print(i)