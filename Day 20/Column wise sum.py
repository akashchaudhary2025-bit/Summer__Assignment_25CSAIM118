# Program to find column-wise sum of a matrix

def column_wise_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sums = []
    
    for j in range(cols):
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        sums.append(col_sum)
    return sums

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of the matrix:")
matrix = [[int(input(f"A[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

result = column_wise_sum(matrix)

print("Column-wise sums:")
for j, s in enumerate(result):
    print(f"Sum of column {j+1}: {s}")
