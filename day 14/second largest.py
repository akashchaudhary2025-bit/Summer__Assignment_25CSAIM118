# Function to find second largest element in array

def second_largest(arr):
    if len(arr) < 2:
        return "Array must have at least two elements"
    
    # Remove duplicates to handle repeated largest values
    unique_arr = list(set(arr))
    
    if len(unique_arr) < 2:
        return "No second largest element (all elements are equal)"
    
    unique_arr.sort(reverse=True)   # sort in descending order
    return unique_arr[1]            # second element is the second largest

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

result = second_largest(arr)
print("Second largest element =", result)
