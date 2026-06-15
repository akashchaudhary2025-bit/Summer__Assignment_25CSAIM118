def nth_fibonacci(n):
    if n <= 0:
        return "Invalid input! n must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Input from user
num = int(input("Enter the position (n): "))

print(f"The {num}th Fibonacci term is {nth_fibonacci(num)}")
