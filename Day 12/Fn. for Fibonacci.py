# Function to generate Fibonacci series

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

num = int(input("Enter the number of terms: "))
print("Fibonacci series up to", num, "terms:", fibonacci(num))
