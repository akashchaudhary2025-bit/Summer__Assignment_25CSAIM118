def largest_prime_factor(n):
   
    largest = -1
    
    
    while n % 2 == 0:
        largest = 2
        n //= 2
    
    
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2
    
    if n > 2:
        largest = n
    
    return largest

number = int(input("Enter a number: "))
print(f"Largest prime factor of {number} is {largest_prime_factor(number)}")
