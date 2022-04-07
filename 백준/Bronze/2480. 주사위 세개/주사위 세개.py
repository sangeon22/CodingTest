a, b, c = map(int, input().split())

if a == b and a == c:
    total = 10000 + a * 1000
elif a == b:
    total = 1000 + a * 100
elif a == c:
    total = 1000 + a * 100
elif b == c:
    total = 1000 + b * 100
else:
    total = max(a, b, c) * 100

print(total)