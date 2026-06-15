# Recursive Factorial Program

def factorial(n):
    if n < 0:
        return "Factorial of negative numbers doesn't exist."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

print(f"Factorial of {num} is:", factorial(num))
