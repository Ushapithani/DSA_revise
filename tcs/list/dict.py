'''input = {'chicken': 300 , 'biryani': 1000 , 'mutton': 500 , 'veg':0}
 output = 1800 
 '''
n = int(input("enter items :"))
items = {}
for i in range(n):
    item , price = input().split()
    items[item] = int(price)
total = 0 
for i in items.values():
    total+=i
print("total", total)