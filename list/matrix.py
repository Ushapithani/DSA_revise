# create a 2d list of 3*4 for all n natural numbers which are divisible by 9 
# print the elemnts row wise
# print the elemnts column wise 
# print matrix and transpose of matrix

size = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
limit = int(input("Enter the maximum natural number to include: "))
matrix = []
current_number = 1
for i in range(size):
    row = []
    for j in range(columns):
        while current_number <= limit:
            if current_number % 9 == 0:
                row.append(current_number)
                current_number += 1
                break
            current_number += 1
    matrix.append(row)
    
print("Matrix:")
for row in matrix:
    print(row)
print("\nElements row-wise:")
for row in matrix:
    for element in row:
        print(element, end=' ')
print()  
print("\nElements column-wise:")
for j in range(columns):
    for i in range(size):
        print(matrix[i][j], end=' ')
    print()  
print("\nTranspose of the matrix:")
transpose = []
for j in range(columns):
    row = []
    for i in range(size):
        row.append(matrix[i][j])
    transpose.append(row)

for row in transpose:
    print(row)
