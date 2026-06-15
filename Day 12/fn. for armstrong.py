# Function to check Armstrong number

def is_armstrong(n):
    
    digits = str(n)
    power = len(digits)
    
   
    total = sum(int(digit) ** power for digit in digits)
    
    return total == n

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
