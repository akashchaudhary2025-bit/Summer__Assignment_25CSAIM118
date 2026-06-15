# Function to move zeros to the end

def move_zeros(arr):
    result = [num for num in arr if num != 0]   # keep non-zero elements
    zeros = [0] * (len(arr) - len(result))      # count how many zeros
    return result + zeros                       # append zeros at the end

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("Original array:", arr)
print("Array after moving zeros to end:", move_zeros(arr))
