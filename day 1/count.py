# Program to count digits in a number

num = int(input("Enter a number: "))

if num < 0:
    num = -num


if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        num //= 10   
        count += 1

print(f"Number of digits = {count}")
