# Program to count set bits in a number

def count_set_bits(n):
    count = 0
    while n > 0:
       
        count += n & 1
   
        n >>= 1
    return count

num = int(input("Enter a number: "))

print("Number of set bits:", count_set_bits(num))
