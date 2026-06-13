# Function to find largest and smallest element in array

def find_min_max(arr):
    smallest = min(arr)   # built-in function to find minimum
    largest = max(arr)    # built-in function to find maximum
    return smallest, largest

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

smallest, largest = find_min_max(arr)

print("Smallest element =", smallest)
print("Largest element =", largest)
