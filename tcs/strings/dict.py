n = int(input())
items = input().split()

counts = {}
for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print(len(counts))
for key in sorted(counts):
    print(key, counts[key])