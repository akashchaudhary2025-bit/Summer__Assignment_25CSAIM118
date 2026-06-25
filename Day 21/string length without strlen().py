# WAP to find string length without using strlen() 

string = input("Enter a string: ")

count = 0
for char in string:
    count += 1

print("Length of the string is:", count)
