numbers = [10, 20, 4, 45, 99]

first = second = numbers[0]
for num in numbers:
    if num >first:
        second = first
        first = num
    elif num >second and num != first:
        second = num

print("Second highest:", second)

# check whether the string anagram or not 
s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("not an anagram")

# all highest count and chaaracter in aa stirng 

s = "programming"
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

max_count = max(freq.values())   
result = {}

for ch in freq:
    if freq[ch] == max_count:    
        result[ch] = freq[ch]

print(result)


# find the non repeating character in the string 
s = "programming"
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
result = []
for ch in freq:
    if freq[ch] == 1:
        result.append(i)
print(result)
    




# find the vowels and consonants in the string 
s = "abcdefghtisdfghjk"
vowel = []
consonant = []

for ch in s:
    if ch in "aeiouAEIOU":
        vowel.append(ch)        
    elif ch.isalpha():          
        consonant.append(ch)

print("Vowels:", vowel)
print("Consonants:", consonant)


# check whether first repeating character is vowel or consonant 
s = "abcdefghtisdfghjk"

vowels = "aeiouAEIOU"
seen = set()

for ch in s:
    if ch in seen:  
        if ch in vowels:
            print(f"First repeating character '{ch}' is a vowel.")
        else:
            print(f"First repeating character '{ch}' is a consonant.")
        break
    seen.add(ch)