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


# 