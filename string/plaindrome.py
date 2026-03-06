# check whether a string is a palindrome or not
string = input("Enter a string: ")
string = string.replace(" ", "").lower()

if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# let us consider a string  i like python programming
#  access the last charcater 
# make string reverse 
# print each character in the string
# print upto python in the string 
# aceess the  each characters in reverse  line by line
# access the alternate characters in the string 
# print the string from like  skipping 3 characters 
string = "i like python programming"

# access the last character
last_character = string[-1]
print("Last character:", last_character)

# make string reverse
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

# print each character in the string
print("Characters in the string:")
for char in string:
    print(char)

# print up to python in the string simple 
index = string.find("python")
if index != -1:
    print("String up to 'python':", string[:index + len("python")])

# access each character in reverse line by line
print("Characters in reverse:")
for char in reversed_string:
    print(char)

# access the alternate characters in the string
print("Alternate characters in the string:")
for i in range(0, len(string), 2):
    print(string[i])

# print the string from like skipping 3 characters
print("String with every 3rd character skipped:")
for i in range(1, len(string), 4):
    print(string[i])