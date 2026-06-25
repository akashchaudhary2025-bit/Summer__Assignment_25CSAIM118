# WAP to convert lowercase letters to uppercase

string = input("Enter a string: ")

result = ""
for char in string:

    if 'a' <= char <= 'z':
        
        result += chr(ord(char) - 32)
    else:
        result += char

print("Converted string:", result)
