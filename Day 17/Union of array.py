# Program to find union of two arrays

def union_arrays(arr1, arr2):
    # Using set to remove duplicates
    union = list(set(arr1) | set(arr2))
    return union

n1 = int(input("Enter number of elements in first array: "))
arr1 = list(map(int, input("Enter elements of first array: ").split()))

n2 = int(input("Enter number of elements in second array: "))
arr2 = list(map(int, input("Enter elements of second array: ").split()))

result = union_arrays(arr1, arr2)
print("Union of arrays:", result)
