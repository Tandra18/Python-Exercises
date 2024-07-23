def factorial(n):
    if n == 0 or n == 1:
        return 1

    fact_result = 1

    for i in range(2, n+1):
        fact_result *= i
    return fact_result

number = 5
print(f"The factorail of {number} is :", factorial(number))
