from sys import stdin

while True:
    # try:

    N = stdin.readline().rstrip("\n")
    count = [0] * 4

    # A, B, C, D = 0, 0, 0, 0
    # for i in N:
    #     if 'a' <= i <= 'z':
    #         A += 1
    #     elif 'A' <= i <= 'Z':
    #         B += 1
    #     elif i == ' ':
    #         D += 1
    #     else:
    #         C += 1
    # print(A, B, C, D)

    if not N:
        break

    for i in N:
        if i.islower():
            count[0] += 1
            # A += 1
        elif i.isupper():
            count[1] += 1
            # B += 1
        elif i.isdigit():
            count[2] += 1
            # D += 1
        else:
            count[3] += 1
            # C += 1
    print(*count)
    # print(A, B, C, D)



