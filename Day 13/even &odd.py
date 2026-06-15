# Function to count even and odd numbers in array

def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count, odd_count

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

even, odd = count_even_odd(arr)

print("Number of even elements =", even)
print("Number of odd elements =", odd)
