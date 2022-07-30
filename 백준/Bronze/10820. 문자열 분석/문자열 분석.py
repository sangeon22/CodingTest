import sys

while True:
    line = sys.stdin.readline().rstrip("\n")
    low, up, num, space = 0, 0, 0, 0

    if not line:
        break

    for s in line:
        if s.islower():
            low += 1
        elif s.isupper():
            up += 1
        elif s.isdigit():
            num += 1
        elif s.isspace():
            space += 1

    print(low, up, num, space)