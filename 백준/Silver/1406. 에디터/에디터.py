from sys import stdin

l = list(map(str, stdin.readline().rstrip()))
r = []
m = int(stdin.readline())

for i in range(m):
    command = stdin.readline().split()
    if command[0] == 'L':
        if len(l) == 0:
            continue
        r.append(l.pop())

    elif command[0] == 'D':
        if len(r) == 0:
            continue
        l.append(r.pop())

    elif command[0] == 'B':
        if len(l) == 0:
            continue
        l.pop()

    elif command[0] == 'P':
        l.append(command[1])
r.reverse()
l.extend(r)
print("".join(l))
