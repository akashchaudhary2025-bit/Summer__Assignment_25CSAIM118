# WAP to find the first non-repeating character in a string

string = input("Enter a string: ")

freq = {}


for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1


first_non_repeating = None
for char in string:
    if freq[char] == 1:
        first_non_repeating = char
        break

if first_non_repeating:
    print("First non-repeating character is:", first_non_repeating)
else:
    print("No non-repeating character found")
