# Program to merge two arrays

def merge_arrays(arr1, arr2):
    return arr1 + arr2   # concatenates both arrays

n1 = int(input("Enter number of elements in first array: "))
arr1 = list(map(int, input("Enter elements of first array: ").split()))

n2 = int(input("Enter number of elements in second array: "))
arr2 = list(map(int, input("Enter elements of second array: ").split()))

merged = merge_arrays(arr1, arr2)
print("Merged array:", merged)
