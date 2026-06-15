# Program to convert decimal to binary

def decimal_to_binary(n):
   
    return bin(n).replace("0b", "")


num = int(input("Enter a decimal number: "))

print("Binary representation:", decimal_to_binary(num))
