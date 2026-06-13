# Function to find duplicates in array

def find_duplicates(arr):
    duplicates = []
    seen = set()
    
    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)
    
    return duplicates

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

dup = find_duplicates(arr)

if dup:
    print("Duplicate elements are:", dup)
else:
    print("No duplicates found")
