# Star Pyramid Pattern

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Each row has (2*i - 1) stars
    print("*" * (2 * i - 1))
