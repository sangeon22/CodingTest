from sys import stdin

n = int(stdin.readline())

li = list(map(int, stdin.readline().split()))
li_s = sorted(set(li))

dic = {li_s[i] : i for i in range(len(li_s))}

for i in li:
    print(dic[i], end=" ")
