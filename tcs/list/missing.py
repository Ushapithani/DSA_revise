# find missing number 
numbers = list(map(int, input().split()))
n = len(numbers)+1
expected = n*(n+1)//2
actual_sum = sum(numbers)
missing = expected-actual_sum
print("expected_number:",missing)
