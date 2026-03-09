nums = [1, 2, 4, 5, 6, 3, 7]
target = 7
num_map = {}  

for index, num in enumerate(nums):
    diff = target - num
    if diff in num_map:
        print(diff, num)  
    num_map[num] = index

