# a,b,c 다 같음 a == b , a == c
# a b만 같음 a == b, a != c
# a c만 같음 a == c, a != b
# b c만 같음 b == c, a != b
# 다다름 a != b, a != c
n = int(input())
total = []

for i in range(n):
    temp = 0
    a, b, c = map(int, input().split())
    if a == b == c:
        total.append(10000 + a * 1000)
    elif a == b:
        total.append(1000 + a * 100)
    elif a == c:
        total.append(1000 + a * 100)
    elif b == c:
        total.append(1000 + b * 100)
    else:
        total.append(max(a, b, c) * 100)

print(max(total))
