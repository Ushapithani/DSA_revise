# input = [1,2,3] & [1,2,3] = true 
# input = [1,2,3] & [3,2,1] = false 
def lists_equal(a, b):
    return a == b

print(lists_equal([1,2,3], [1,2,3]))  # True
print(lists_equal([1,2,3], [3,2,1]))  # False
