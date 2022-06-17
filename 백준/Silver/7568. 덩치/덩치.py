from sys import stdin

n = int(stdin.readline())

a = []
r = []

for i in range(n):
    x, y = map(int, stdin.readline().split())
    a.append((x, y))

for i in range(n):
    count = 0
    for j in range(n):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            count += 1
    r.append(count + 1)

print(*r)