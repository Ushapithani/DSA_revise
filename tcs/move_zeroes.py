# move zeroes to end 
numbers = list(map(int, input().split()))
pos = 0 
for i in range(len(numbers)):
    if numbers[i]!=0:
        numbers[pos], numbers[i] = numbers[i], numbers[pos]
        pos+=1
print(numbers)