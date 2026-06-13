# Program to calculate x^n without using pow()

def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

x = int(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))

print(f"{x}^{n} =", power(x, n))
