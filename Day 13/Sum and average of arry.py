# Function to calculate sum and average of array

def sum_and_average(arr):
    total = sum(arr)              # built-in sum function
    average = total / len(arr)    # divide by number of elements
    return total, average

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

total, avg = sum_and_average(arr)

print("Sum of array =", total)
print("Average of array =", avg)
