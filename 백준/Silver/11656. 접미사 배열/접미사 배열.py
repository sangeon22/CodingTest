from sys import stdin

S = stdin.readline().rstrip("\n")
word = []
for i in range(len(S)):
    word.append(S[i::1])

word.sort()

for i in word:
    print(i)