'''Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4'''
numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for index in range(len(numbers)):
    if numbers[index] == target:
        print("Target found at index", index)
        break
else:
    print("Target not found")