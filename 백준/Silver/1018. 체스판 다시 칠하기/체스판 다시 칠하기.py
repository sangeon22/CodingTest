from sys import stdin

n, m = map(int, stdin.readline().split())
li = []
total = []

for i in range(n):
    li.append(stdin.readline())

for i in range(n - 7):
    for j in range(m - 7):
        white = 0
        black = 0

        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 != 0:
                    if li[k][l] != 'W':
                        white += 1
                    if li[k][l] != 'B':
                        black += 1
                else:
                    if li[k][l] != 'B':
                        white += 1
                    if li[k][l] != 'W':
                        black += 1
        total.append(white)
        total.append(black)

print(min(total))