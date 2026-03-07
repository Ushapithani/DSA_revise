# let us consider an input as fruits check wheter the lenght of fruit is greater than 5 characters move tto the list at even index the length f flowers input is less than 10 characters move to the same list at odd index the input should be opposite case 
# flowers = [ "rose", "lily", "tulip", "daisy", "sunflower"]
# fruits =[ "banana", "orange", "grape", "apple", "kiwi"]
# output should be  ["BANANA", "rose", "ORANGE", "lily", "GRAPE", "tulip", "APPLE", "daisy", "NUll ", "sunflower"]

final_list = []
n=int(input("enter the size of fruits:"))
flower_size= 0
fruit_size=1
for i in range(n):
    fruit=input("enter the fruit name:")
    if len(fruit)>5:
        final_list.append(fruit.swapcase())
    else:
        final_list.append('null')
    fruit_size+=2
    flower=input("enter the flower name:")
    if len(flower)<10:
        final_list.append(flower.swapcase())
    else:
        final_list.append('null')
    flower_size+=2
print(final_list)

