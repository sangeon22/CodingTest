from sys import stdin


def push(x):
    queue.append(x)


def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.pop(0))


def size():
    print(len(queue))


def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)


def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])


def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])


queue = []
N = int(stdin.readline())
for i in range(N):
    a = stdin.readline().split()

    if a[0] == "push":
        push(a[1])
    elif a[0] == "pop":
        pop();
    elif a[0] == "size":
        size();
    elif a[0] == "empty":
        empty()
    elif a[0] == "front":
        front()
    elif a[0] == "back":
        back()
