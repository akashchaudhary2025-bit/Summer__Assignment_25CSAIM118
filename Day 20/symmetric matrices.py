# Program to check if a matrix is symmetric

def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows != cols:
        return False  
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

n = int(input("Enter size of square matrix (n x n): "))

print("Enter elements of the matrix:")
matrix = [[int(input(f"A[{i}][{j}]: ")) for j in range(n)] for i in range(n)]

if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
