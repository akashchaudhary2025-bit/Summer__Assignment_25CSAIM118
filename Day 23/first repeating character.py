# WAP to find the first repeating character in a string

string = input("Enter a string: ")

seen = set()
first_repeating = None

for char in string:
    if char in seen:
        first_repeating = char
        break
    else:
        seen.add(char)

if first_repeating:
    print("First repeating character is:", first_repeating)
else:
    print("No repeating character found")
