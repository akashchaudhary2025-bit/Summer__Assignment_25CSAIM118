# Character Triangle Pattern

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(65, 65 + i):   # ASCII value of 'A' is 65
        print(chr(j), end=" ")
    print()
