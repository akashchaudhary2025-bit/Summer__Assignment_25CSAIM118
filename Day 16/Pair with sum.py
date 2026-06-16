# Program to find pairs with given sum

def find_pairs(arr, target):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
target = int(input("Enter the target sum: "))

result = find_pairs(arr, target)

if result:
    print("Pairs with given sum:")
    for p in result:
        print(p)
else:
    print("No pairs found.")
