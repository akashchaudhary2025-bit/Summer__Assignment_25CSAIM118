# Program to transpose a matrix

def transpose_matrix(A):
    rows = len(A)
    cols = len(A[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = A[i][j]
    return result

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of the matrix:")
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

T = transpose_matrix(A)

print("Transpose of the matrix:")
for row in T:
    print(row)
