# Repeated Character Pattern

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # chr(65) = 'A', so chr(65 + i - 1) gives the ith letter
    print((chr(64 + i) + " ") * i)
