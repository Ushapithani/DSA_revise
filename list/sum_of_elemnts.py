# sum of elements 
def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total
# Example 
numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers)
print("The sum of the elements is:", result)


# sum of elements in a 2d list
def sum_of_elements_2d(lst):
    total = 0
    for row in lst:
        for num in row:
            total += num
    return total
# Example
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result_2d = sum_of_elements_2d(two_d_list)
print("The sum of the elements in the 2D list is:", result_2d)


# max element in a list
def max_element(lst):
    if not lst:
        return None  
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num
# Example
numbers = [1, 2, 3, 4, 5]
max_num = max_element(numbers)
print("The maximum element is:", max_num)


# max element in a 2d list
def max_element_2d(lst):
    if not lst:
        return None  
    max_num = lst[0][0]
    for row in lst:
        for num in row:
            if num > max_num: 
                max_num = num
    return max_num

# Example
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_num_2d = max_element_2d(two_d_list)
print("The maximum element in the 2D list is:", max_num_2d) 


# min elemnent in a 2d list 
def min_element_2d(lst):
    if not lst:
        return None  
    min_num = lst[0][0]
    for row in lst:
        for num in row:
            if num < min_num: 
                min_num = num
    return min_num
# Example
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
min_num_2d = min_element_2d(two_d_list)
print("The minimum element in the 2D list is:", min_num_2d)