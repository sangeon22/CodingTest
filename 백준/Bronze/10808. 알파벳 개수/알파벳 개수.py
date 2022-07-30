from sys import stdin

S = stdin.readline().rstrip()
idx = []
count = [0] * 26

for i in S:
    idx.append(ord(i)-ord('a'))

for j in idx:
    count[j] += 1
print(*count)