from sys import stdin

n = int(stdin.readline())
a = []

for i in range(n):
    x, y = map(int, stdin.readline().split())
    a.append((x, y))
a.sort()
for i in a:
    print(*i)