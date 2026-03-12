n = int(input())
matrix = []
for i in range(n):
    row = input().split()
    matrix.append(row)
for row in range(n):
    for col in range (n):
        matrix[row], matrix[col] = matrix[col],matrix[row]
print(matrix) 

