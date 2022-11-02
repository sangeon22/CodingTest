from sys import stdin

answer = []
li1 = [1, 1, 2, 2, 2, 8]
li2 = list(map(int, stdin.readline().split()))

for i in range(len(li1)):
    answer.append(li1[i] - li2[i])

print(*answer)