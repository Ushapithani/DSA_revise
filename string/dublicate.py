string = input()
seen = []
for i in range(len(string)):
    if string[i] not in seen:
        seen.append(string[i])
print("".join(seen))


# input : aaaaabbbbbbbccccccc
# output :abc
