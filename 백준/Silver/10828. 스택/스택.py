from sys import stdin

stack = []
N = int(stdin.readline())


def push(x):
    stack.append(x)


def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())


def size():
    print(len(stack))


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


for i in range(N):
    a = stdin.readline().split()
    if a[0] == "push":
        push(a[1])
    elif a[0] == "pop":
        pop()
    elif a[0] == "size":
        size()
    elif a[0] == "empty":
        empty()
    elif a[0] == "top":
        top()
