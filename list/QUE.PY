# CRAETE A 3D LIST OF ALL ODD NUMBERS AND FIND THE SUM OF NUMBERS , COUNT OF NUMBERS , MAX , MIN 
list1 = [[[1, 3, 5], [7, 9, 11]], [[13, 15, 17], [19, 21, 23]], [[25, 27, 29], [31, 33, 35]]]
size = int(input("Enter the size of each dimension (e.g., 3 for 3x3x3 cube): "))
limit = int(input("Enter the maximum odd number to include: "))

list1 = []
current_number = 1

for i in range(size):
    layer = []
    for j in range(size):
        row = []
        for k in range(size):
            if current_number <= limit:
                row.append(current_number)
                current_number += 2
        layer.append(row)
    list1.append(layer)

print("\n3D List of Odd Numbers:")
print(list1)

sum_of_numbers = 0
count_of_numbers = 0
max_number =list1[0][0][0]  
min_number = list1[0][0][0]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        for k in range(len(list1[i][j])):
            number = list1[i][j][k]
            sum_of_numbers += number
            count_of_numbers += 1
            if number > max_number:
                max_number = number
            if number < min_number:
                min_number = number

print("Sum of numbers:", sum_of_numbers)
print("Count of numbers:", count_of_numbers)
print("Maximum number:", max_number)
print("Minimum number:", min_number)

