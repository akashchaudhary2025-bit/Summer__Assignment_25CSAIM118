# Input and Display Array

def input_array():
    n = int(input("Enter the number of elements: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
    return arr

def display_array(arr):
    print("Array elements are:")
    for element in arr:
        print(element, end=" ")

array = input_array()
display_array(array)
