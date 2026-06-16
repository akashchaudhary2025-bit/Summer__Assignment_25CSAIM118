# Program to find maximum frequency element

def max_frequency_element(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    
    max_elem = max(freq, key=freq.get)
    return max_elem, freq[max_elem]

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

element, count = max_frequency_element(arr)
print(f"Element with maximum frequency: {element} (occurs {count} times)")
