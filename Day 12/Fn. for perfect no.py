# Function to check Perfect Number

def is_perfect(n):
    if n < 1:
        return False
    
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    
    return divisors_sum == n

num = int(input("Enter a number: "))

if is_perfect(num):
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
