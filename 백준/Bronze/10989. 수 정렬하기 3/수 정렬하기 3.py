from sys import stdin

n = int(stdin.readline())
li = [0] * 10001
for _ in range(n):
    a = stdin.readline()
    li[int(a)] += 1

for i in range(1, 10001):
    if li[i] >= 1:
        for _ in range(li[i]):
            print(i)