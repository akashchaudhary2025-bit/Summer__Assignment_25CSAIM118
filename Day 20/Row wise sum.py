# Program to find row-wise sum of a matrix

def row_wise_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sums = []
    
    for i in range(rows):
        row_sum = 0
        for j in range(cols):
            row_sum += matrix[i][j]
        sums.append(row_sum)
    return sums

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of the matrix:")
matrix = [[int(input(f"A[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

result = row_wise_sum(matrix)

print("Row-wise sums:")
for i, s in enumerate(result):
    print(f"Sum of row {i+1}: {s}")
