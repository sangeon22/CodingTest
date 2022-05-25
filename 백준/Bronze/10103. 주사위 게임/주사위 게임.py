n = int(input())
a = 100
b = 100

for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        b -= x
    elif x < y:
        a -= y
    else:
        continue

print(a)
print(b)
