arr = list(map(int, input("Enter numbers: ").split()))

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Sorted:", arr)
```

**Output:**
```
Enter numbers: 38 27 43 3 9 82 10
Sorted: [3, 9, 10, 27, 38, 43, 82]