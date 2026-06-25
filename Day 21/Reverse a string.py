# WAP to reverse a string

string = input("Enter a string: ")


reversed_string = string[::-1]
print("Reversed string (slicing):", reversed_string)


rev = ""
for char in string:
    rev = char + rev
print("Reversed string (loop):", rev)
