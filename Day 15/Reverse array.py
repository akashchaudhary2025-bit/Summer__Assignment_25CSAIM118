# Function to reverse an array

def reverse_array(arr):
    return arr[::-1]   # slicing method to reverse

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("Original array:", arr)
print("Reversed array:", reverse_array(arr))
