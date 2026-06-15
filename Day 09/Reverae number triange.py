# Reverse Number Triangle Pattern

rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):   # Start from rows down to 1
    for j in range(1, i + 1):  # Print numbers from 1 to i
        print(j, end=" ")
    print()
