n = int(input("enter numbers: "))          
target = int(input("enter target : "))    
numbers = list(map(int, input().split())) 

number_set = {}
for num in numbers:
    diff = target - num
    if diff in number_set:
        print("the sum of two numbers:  ",diff, num)   
        break              
    number_set[num] = True