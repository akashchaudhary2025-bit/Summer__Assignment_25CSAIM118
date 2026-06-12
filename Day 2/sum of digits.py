# Program to find sum of digits of a number

num = int(input("Enter a number: "))
sum_digits = 0


if num < 0:
    num = -num

while num > 0:
    digit = num % 10      
    sum_digits += digit   
    num //= 10             

print("Sum of digits =", sum_digits)
