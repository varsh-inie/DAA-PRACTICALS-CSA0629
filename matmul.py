# Input matrix A
A = [[int(x) for x in input("Enter elements of matrix A separated by space: ").split()] for _ in range(int(input("Enter number of rows for matrix A: ")))]

# Input matrix B
B = [[int(x) for x in input("Enter elements of matrix B separated by space: ").split()] for _ in range(int(input("Enter number of rows for matrix B: ")))]

# Check if matrices can be multiplied
if len(A[0]) != len(B):
    print("Matrices cannot be multiplied: Invalid dimensions")
    exit()

# Perform matrix multiplication
C = [[0] * len(B[0]) for _ in range(len(A))]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

# Print the result matrix
print("Resultant matrix (A x B):")
for row in C:
    print(" ".join(map(str, row)))
