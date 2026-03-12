# Take matrix input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter matrix elements row by row:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Transpose
transpose = [[0] * rows for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

print("Transpose of the matrix:")
for row in transpose:
    print(row)