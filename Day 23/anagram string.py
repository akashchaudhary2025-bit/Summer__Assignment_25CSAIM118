# WAP to check if two strings are anagrams

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()


if sorted(str1) == sorted(str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")


freq1 = {}
freq2 = {}

for char in str1:
    freq1[char] = freq1.get(char, 0) + 1

for char in str2:
    freq2[char] = freq2.get(char, 0) + 1

if freq1 == freq2:
    print("The strings are anagrams (dictionary method)")
else:
    print("The strings are not anagrams (dictionary method)")
