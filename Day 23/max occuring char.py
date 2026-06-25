# WAP to find maximum occurring character in a string

string = input("Enter a string: ")

freq = {}


for char in string:
    freq[char] = freq.get(char, 0) + 1


max_char = max(freq, key=freq.get)
print("Maximum occurring character is:", max_char)
print("It occurs", freq[max_char], "times")
