# create a n^3 element  of 2d list














# print row wise and column wise element of 2d list
def print_row_wise(lst):
    for row in lst:
        print(row)
def print_column_wise(lst):
    if not lst:
        return
    num_columns = len(lst[0])
    for col in range(num_columns):
        column_elements = []
        for row in lst:
            column_elements.append(row[col])
        print(column_elements)
# Example
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Row-wise elements:")
print_row_wise(two_d_list)
print("Column-wise elements:")
print_column_wise(two_d_list)


# count of even numbers in a 2d list
def count_even_numbers_2d(lst):
    count = 0
    for row in lst:
        for num in row:
            if num % 2 == 0:
                count += 1
    return count

# Example
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_count = count_even_numbers_2d(two_d_list)

print("The count of even numbers in the 2D list is:", even_count) # 4 

# count of numbers 
def count_numbers_2d(lst):
    count = 0
    for row in lst:
        for num in row:
            count += 1
    return count
# Example
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
number_count = count_numbers_2d(two_d_list)
print("The count of numbers in the 2D list is:", number_count) # 9


