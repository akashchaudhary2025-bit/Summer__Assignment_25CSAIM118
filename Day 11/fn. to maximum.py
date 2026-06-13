# Function to find maximum of two numbers

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Maximum =", find_max(num1, num2))
