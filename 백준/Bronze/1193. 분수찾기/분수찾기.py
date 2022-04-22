# 분자 / 분모
# 1 - 1             1
# 2 - 1 2           2 1
# 3 - 3 2 1         1 2 3
# 4 - 1 2 3 4       4 3 2 1
# 5 - 5 4 3 2 1     1 2 3 4 5

X = int(input())
line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line-X+1
else:
    a = line-X+1
    b = X

print(a, '/', b, sep='')