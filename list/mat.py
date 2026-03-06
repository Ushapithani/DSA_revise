
# create a 2d list of 2*3*4 for all n natural numbers which are divisible by 9

def create_3d_list(x, y, z):
    three_d_list = []
    for i in range(x):
        two_d_list = []
        num = 1
        for j in range(y):
            row = []
            for k in range(z):
                while num % 9 != 0:
                    num += 1
                row.append(num)
                num += 1
            two_d_list.append(row)
        three_d_list.append(two_d_list)
    return three_d_list

def create_row_wise():
    for row in  three_d_matrix:
        print(row)
def create_c


