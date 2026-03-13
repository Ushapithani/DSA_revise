'''90 degress  trans+revsre wows
180 reverse rows +reverse colums 
270 tranpose + reverse colums'''
''' 

Input:
3
1 2 3
4 5 6
7 8 9

Output:
7 4 1
8 5 2
9 6 3
'''
# rotate matrix by 90 degrees => transpose +reverse rows 
n = int(input())
matrix = []
for i in range(n):
    row = input().split()
    matrix.append(row)
# 90 
rotated =[]
for col in range(n):
    new_row = []
    for row in range(n-1,-1,-1):
        new_row.append(matrix[row][col])
    rotated.append(new_row)

# print
for row in rotated:
    print(" ".join(row))

# 180 degrees
'''
3
1 2 3
4 5 6
7 8 9
output 
9 8 7
6 5 4
3 2 1'''
n = int(input())
matrix = []
for i in range(n):
    row = input().split()
    matrix.append(row)

# Rotate 180 degrees 
rotated = []
for row in range(n-1, -1, -1):       
    new_row = []
    for col in range(n-1, -1, -1):   
        new_row.append(matrix[row][col])
    rotated.append(new_row)

# Print rotated matrix
for row in rotated:
    print(" ".join(row))


'''
270 
ip
3
1 2 3
4 5 6
7 8 9
op
3 6 9
2 5 8
1 4 7
'''

n = int(input())
matrix = []
for i in range(n):
    row = input().split()
    matrix.append(row)

# Rotate 270 degrees clockwise => transpose + reverse colums
rotated = []
for col in range(n-1, -1, -1):       
    new_row = []
    for row in range(n):             
        new_row.append(matrix[row][col])
    rotated.append(new_row)

# Print rotated matrix
for row in rotated:
    print(" ".join(row))