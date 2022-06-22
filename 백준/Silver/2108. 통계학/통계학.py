from sys import stdin
from collections import Counter


def avg(li, n):
    print(round(sum(li) / n))


def mid(li, n):
    print(li[n//2])


def many(li):
    cnt = Counter(li).most_common()
    if len(cnt) > 1:
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0])
        else:
            print(cnt[0][0])
    else:
        print(cnt[0][0])


def ran(li):
    print(max(li) - min(li))


n = int(stdin.readline())
li = []
for _ in range(n):
    li.append(int(stdin.readline().strip()))

li.sort()

avg(li, n)
mid(li, n)
many(li)
ran(li)
