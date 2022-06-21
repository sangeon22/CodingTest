from sys import stdin

n = int(stdin.readline())
a = []

for i in range(n):
    x, y = map(int, stdin.readline().split())
    a.append((y, x))

a.sort()

for y, x in a:
    print(x,y)
