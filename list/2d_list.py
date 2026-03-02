# create a n^3 element  of 2d list

n = 3

two_d_list = []

for i in range(n):
    row = []
    for j in range(n**2):
        row.append(i * n**3 + j)
    two_d_list.append(row)

for row in two_d_list:
    print(row)
    