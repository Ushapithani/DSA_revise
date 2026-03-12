'''Input: s = "anagram", t = "nagaram" → Output: true
Input: s = "rat", t = "car" → Output: false'''

s1 = input()
s2 = input()
if sorted(s1) == sorted(s2):
    print("true")
else:
    print("false")