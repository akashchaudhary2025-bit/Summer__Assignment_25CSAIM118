# Program to check whether a number is palindrome

num = int(input("Enter a number: "))
original = num
reversed_num = 0

# Work with positive numbers
temp = abs(num)

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

if num < 0:
    reversed_num = -reversed_num

if original == reversed_num:
    print(original, "is a palindrome number.")
else:
    print(original, "is not a palindrome number.")
