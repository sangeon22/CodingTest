from sys import stdin

T = int(stdin.readline())
for i in range(T):
    a = stdin.readline()
    li = list(a)
    cnt = 0

    for j in li:
        if j == '(':
            cnt += 1
        elif j == ')':
            cnt -= 1

        if cnt < 0:
            print("NO")
            break

    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")