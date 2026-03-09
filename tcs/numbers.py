''' input = 
1 2 3 
4 5 6 
7 8 9 
output = 
3 2 1 
6 5 4
9 8 7 
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    row.reverse()

for row in matrix:
    print(*row)



# user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in matrix:
    row.reverse()

for row in matrix:
    print(*row)