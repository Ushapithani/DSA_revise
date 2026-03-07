# string  web developemnt intergrated with ai make half of the string revrerse and second shold be same and print the string
string = "web development integrated with ai"
lenght = len(string)
half_lenght = lenght//2
first_half = string [ :half_lenght]
second_half = string[half_lenght :]
reversed_first_half = first_half[::-1]
print(reversed_first_half + second_half)


# create a string apple check whether the present in the list of fruits or not
fruits = ["banana", "orange", "grape", "apple", "kiwi"]
apple = "apple"

if apple in fruits:
    print(f"{apple} is in the list of fruits")
else:
    print(f"{apple} is not in the list of fruits")


# convert captital letters into small letters without using lower function
string = "HELLO WORLD"
converted_string = ""
for char in string:
    if 'A' <= char <= 'Z':
        converted_string += chr(ord(char) + 32)
    else:
        converted_string += char

print("Converted string:", converted_string)

# Find minimum number of character deletions to make two strings equal
def min_deletions_to_make_equal(str1, str2):
    from collections import Counter

    count1 = Counter(str1)
    count2 = Counter(str2)

    deletions = 0

    for char in set(str1 + str2):
        deletions += abs(count1[char] - count2[char])

    return deletions
min
