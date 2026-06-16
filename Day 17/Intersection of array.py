# Program to find intersection of two arrays

def intersection_arrays(arr1, arr2):
    
    return list(set(arr1) & set(arr2))

n1 = int(input("Enter number of elements in first array: "))
arr1 = list(map(int, input("Enter elements of first array: ").split()))

n2 = int(input("Enter number of elements in second array: "))
arr2 = list(map(int, input("Enter elements of second array: ").split()))

result = intersection_arrays(arr1, arr2)
print("Intersection of arrays:", result)
