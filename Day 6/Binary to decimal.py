# Program to convert binary to decimal

def binary_to_decimal(binary_str):
    
    return int(binary_str, 2)

binary_num = input("Enter a binary number: ")

print("Decimal representation:", binary_to_decimal(binary_num))
