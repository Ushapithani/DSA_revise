# input = ['dsa', 'dev', 'devops' ,'','ai',None]
# output = ['dsa','dev','devops','ai']

user_input = input("Enter values separated by space: ").split()

result = []
for item in user_input:
    if item != '' and item.lower() != 'none':
        result.append(item)

print(result)