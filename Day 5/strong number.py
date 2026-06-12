def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_strong(num):
    digits = str(num)
    total = sum(factorial(int(digit)) for digit in digits)
    return total == num

number = int(input("Enter a number: "))

if is_strong(number):
    print(f"{number} is a Strong Number.")
else:
    print(f"{number} is not a Strong Number.")
