from sys import stdin

n = int(stdin.readline())
a = []

for i in range(n):
    a.append(stdin.readline().strip())

a = set(a)
a = list(a)

a.sort()
a.sort(key=len)

for i in a:
    print(i)
