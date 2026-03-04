def create_3d_list(layer, y, z):
    three_d_list = []
    for i in range(layer):
        two_d_list = []
        for j in range(y):
            one_d_list = []
            for k in range(z):
                one_d_list.append(0)  
            two_d_list.append(one_d_list)
        three_d_list.append(two_d_list)
    return three_d_list
# Example 
three_d_list = create_3d_list(1, 3, 4)
print(three_d_list)
for layer in three_d_list:
    for row in layer:
        print(row)



# 
