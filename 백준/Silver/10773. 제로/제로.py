from sys import stdin

K = int(stdin.readline())
total = []

for i in range(K):
    a = int(stdin.readline())
    if a == 0:
        total.pop()
    else:
        total.append(a)

print(sum(total))

