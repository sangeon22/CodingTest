from sys import stdin
from collections import deque

d = deque()
n = int(stdin.readline())


def push_front(x):
    d.appendleft(x)


def push_back(x):
    d.append(x)


def pop_front():
    if len(d) == 0:
        return -1
    else:
        return d.popleft()


def pop_back():
    if len(d) == 0:
        return -1
    else:
        return d.pop()


def size():
    return len(d)


def empty():
    if len(d) == 0:
        print(1)
    else:
        print(0)


def front():
    if len(d) == 0:
        print(-1)
    else:
        print(d[0])


def back():
    if len(d) == 0:
        print(-1)
    else:
        print(d[-1])


# def front():
#     return d.


for i in range(n):
    x = stdin.readline().split()
    if x[0] == "push_front":
        push_front(x[1])
    elif x[0] == "push_back":
        push_back(x[1])
    elif x[0] == "pop_front":
        print(pop_front())
    elif x[0] == "pop_back":
        print(pop_back())
    elif x[0] == "size":
        print(size())
    elif x[0] == "empty":
        empty()
    elif x[0] == "front":
        front()
    elif x[0] == "back":
        back()
