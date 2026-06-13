# Recursive Fibonacci Program

def fibonacci(n):
    if n <= 0:
        return "Invalid input! n must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter the number of terms: "))

print(f"Fibonacci series up to {num} terms:")
for i in range(1, num + 1):
    print(fibonacci(i), end=" ")
