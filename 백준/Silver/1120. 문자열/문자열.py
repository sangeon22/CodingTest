a, b = map(str, input().split())
d = len(b) - len(a)
min_diff = float('inf')

if len(a) > len(b):
    min_diff = len(a) - len(b)
else:
    for i in range(len(b) - len(a) + 1):
        diff = sum(1 for x, y in zip(a, b[i:i+len(a)]) if x != y)
        min_diff = min(min_diff, diff)

print(min_diff)
