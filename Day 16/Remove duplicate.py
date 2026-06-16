# Program to remove duplicates from array

def remove_duplicates(arr):
    unique = []
    for num in arr:
        if num not in unique:
            unique.append(num)
    return unique

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

result = remove_duplicates(arr)
print("Array after removing duplicates:", result)
