# Function to rotate array right by k positions

def rotate_right(arr, k):
    n = len(arr)
    k = k % n   # handle cases where k > n
    return arr[-k:] + arr[:-k]

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

k = int(input("Enter number of positions to rotate right: "))

rotated = rotate_right(arr, k)

print("Original array:", arr)
print(f"Array after right rotation by {k} positions:", rotated)
