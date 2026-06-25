# WAP to check if two strings are rotations of each other

def is_rotation(str1, str2):
    
    if len(str1) != len(str2):
        return False
    
    
    temp = str1 + str1
    
    
    return str2 in temp


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if is_rotation(s1, s2):
    print("The strings are rotations of each other")
else:
    print("The strings are NOT rotations of each other")
