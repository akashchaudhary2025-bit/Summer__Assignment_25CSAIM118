# Program to find diagonal sum of a matrix

def diagonal_sum(matrix):
    n = len(matrix)
    primary = 0
    secondary = 0
    
    for i in range(n):
        primary += matrix[i][i]           
        secondary += matrix[i][n - i - 1]
    
    return primary, secondary

n = int(input("Enter size of square matrix (n x n): "))

print("Enter elements of the matrix:")
matrix = [[int(input(f"A[{i}][{j}]: ")) for j in range(n)] for i in range(n)]

primary, secondary = diagonal_sum(matrix)

print("Sum of primary diagonal:", primary)
print("Sum of secondary diagonal:", secondary)
