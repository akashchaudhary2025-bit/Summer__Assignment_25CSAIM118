# Program to subtract two matrices

def subtract_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] - B[i][j]
    return result

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

print("Enter elements of second matrix:")
B = [[int(input(f"B[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

C = subtract_matrices(A, B)

print("Resultant Matrix after Subtraction:")
for row in C:
    print(row)
