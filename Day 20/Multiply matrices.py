# Program to multiply two matrices

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

   
    if cols_A != rows_B:
        print("Matrix multiplication not possible!")
        return None

    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

rows_A = int(input("Enter number of rows for Matrix A: "))
cols_A = int(input("Enter number of columns for Matrix A: "))
print("Enter elements of Matrix A:")
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(cols_A)] for i in range(rows_A)]

rows_B = int(input("Enter number of rows for Matrix B: "))
cols_B = int(input("Enter number of columns for Matrix B: "))
print("Enter elements of Matrix B:")
B = [[int(input(f"B[{i}][{j}]: ")) for j in range(cols_B)] for i in range(rows_B)]

C = multiply_matrices(A, B)

if C:
    print("Resultant Matrix after Multiplication:")
    for row in C:
        print(row)
