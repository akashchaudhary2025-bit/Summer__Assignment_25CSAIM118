# Function to check palindrome number

def is_palindrome(n):
    original = str(n)         
    reversed_num = original[::-1]  
    return original == reversed_num

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
