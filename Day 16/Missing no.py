# Program to find missing number in array

def find_missing(arr, n):
    total = n * (n + 1) // 2   
    sum_arr = sum(arr)         
    return total - sum_arr     

n = int(input("Enter the size of array (n): "))
arr = list(map(int, input(f"Enter {n-1} elements (from 1 to {n} with one missing): ").split()))

missing = find_missing(arr, n)
print("Missing number is:", missing)
