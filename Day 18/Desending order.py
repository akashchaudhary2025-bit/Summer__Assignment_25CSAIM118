# Program to sort array in descending order

def sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:   # swap if smaller
                arr[i], arr[j] = arr[j], arr[i]
    return arr

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

sorted_arr = sort_descending(arr)
print("Array in descending order:", sorted_arr)
