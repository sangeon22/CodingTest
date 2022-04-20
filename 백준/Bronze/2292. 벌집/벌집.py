# 라인범위   갯수       print      마지막 값
# 1          1          1         1 + 6x0
# 2~7        6          2         1 + 6x1
# 8~19       12         3         1 + 6x3
# 20~37      18         4         1 + 6x6
# 38~61      24         5         1 + 6x10

n = int(input())
line = 1
cnt = 1

for i in range(n):
    line += 6*i
    if n > line:
        cnt += 1
    else:
        break
print(cnt)
