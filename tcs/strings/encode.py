string = input("enter the string: ")

if not string:
    print("")
else:
    result = []
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            if count > 1:
                result.append(string[i-1] + str(count))
            else:
                result.append(string[i-1])
            count = 1
    if count > 1:
        result.append(string[-1] + str(count))
    else:
        result.append(string[-1])
    print("".join(result))
'''

**Output:**
```
enter the string: aaaabbbccaaa
a4b3c2a3   ✅

enter the string: aaaaabbbccccccaaaa
a5b3c6a4   ✅
'''