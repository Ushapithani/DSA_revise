numbers = [10, 20, 4, 45, 99]

first = second = numbers[0]
for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second highest:", second)

# check whether the string anagram or not 
s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("not an anagram")
