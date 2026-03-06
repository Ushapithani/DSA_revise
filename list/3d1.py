def create_3d_list(layer, y, z):
    three_d_list = []
    for i in range(layer):
        two_d_list = []
        for j in range(y):
            one_d_list = []
            for k in range(z):
                one_d_list.append(1) 

            two_d_list.append(one_d_list)
        three_d_list.append(two_d_list)
    return three_d_list
# Example 
three_d_list = create_3d_list(2, 3, 4)
print(three_d_list)
for layer in three_d_list:
    for row in layer:
        print(row)




# max element 
def max_element_3d(lst):
    if not lst:
        return None
    max_element = lst[0][0][0]
    for layer in lst:
        for row in layer:
            for num in row:
                if num > max_element:
                    max_element = num
    return max_element

# row wise and column wise element of 3d list without f string

def print_row_wise_3d(lst):
    for layer in lst:
        for row in layer:
            print(row)
def print_column_wise_3d(lst):
    if not lst or not lst[0] or not lst[0][0]:
        return
    num_layers = len(lst)
    num_rows = len(lst[0])
    num_cols = len(lst[0][0])
    
    for k in range(num_cols):
        print("Column " + str(k) + ":")
        for i in range(num_layers):
            if i < len(lst) and k < len(lst[i][0]):
                print("  Layer " + str(i) + ": " + str(lst[i][0][k]))


# sum of all elements in 3d list
def sum_of_elements_3d(lst):
    total_sum = 0
    for layer in lst:
        for row in layer:
            for num in row:
                total_sum += num
    return total_sum

# count of even numbers in 3d list
def count_even_numbers_3d(lst):
    count = 0
    for layer in lst:
        for row in layer:
            for num in row:
                if num % 2 == 0:
                    count += 1
    return count

#example
three_d_list = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
max_element = max_element_3d(three_d_list)
print("Max element in the 3D list is:", max_element)

even_count = count_even_numbers_3d(three_d_list)
print("Count of even numbers:", even_count)
sum_elements = sum_of_elements_3d(three_d_list)
print("Sum of all elements:", sum_elements)

