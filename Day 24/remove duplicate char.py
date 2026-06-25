# WAP to remove duplicate characters from a string

string = input("Enter a string: ")

result = ""
seen = set()

for char in string:
    if char not in seen:
        result += char
        seen.add(char)

print("String after removing duplicates:", result)

