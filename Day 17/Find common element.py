# Program to find common elements in two arrays

def common_elements(arr1, arr2):
   
    return list(set(arr1) & set(arr2))

n1 = int(input("Enter number of elements in first array: "))
arr1 = list(map(int, input("Enter elements of first array: ").split()))

n2 = int(input("Enter number of elements in second array: "))
arr2 = list(map(int, input("Enter elements of second array: ").split()))

result = common_elements(arr1, arr2)
print("Common elements:", result)
