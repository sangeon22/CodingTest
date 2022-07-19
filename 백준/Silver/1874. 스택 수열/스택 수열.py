from sys import stdin

stack = []
total = []


def push(x):
    stack.append(x)
    return total.append("+")


def pop():
    stack.pop()
    return total.append("-")


count = 0
n = int(stdin.readline())

for i in range(0, n):
    a = int(stdin.readline())

    while count < a:
        count += 1
        push(count)

    if stack[-1] == a:
        pop()

    else:
        print("NO")
        exit(0)


for i in total:
    print(i)