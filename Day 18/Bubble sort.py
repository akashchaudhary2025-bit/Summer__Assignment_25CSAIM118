# Program to perform Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
