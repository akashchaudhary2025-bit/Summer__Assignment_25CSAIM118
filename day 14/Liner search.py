# Function for Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index if found
    return -1          # return -1 if not found

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

target = int(input("Enter the element to search: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at position {result+1}")
else:
    print(f"Element {target} not found in the array")
