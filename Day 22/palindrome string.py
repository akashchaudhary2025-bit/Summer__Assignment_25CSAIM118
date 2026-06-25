# WAP to check palindrome string

string = input("Enter a string: ")

if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


rev = ""
for char in string:
    rev = char + rev

if string == rev:
    print("The string is a palindrome (loop method)")
else:
    print("The string is not a palindrome (loop method)")
