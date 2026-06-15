# Function to find frequency of elements in array

def frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

freq_dict = frequency(arr)

print("Frequency of elements:")
for key, value in freq_dict.items():
    print(f"{key} occurs {value} time(s)")
