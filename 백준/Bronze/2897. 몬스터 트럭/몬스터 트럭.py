# 빌딩('#'), 주차 된 차('X'), 또는 빈 주차 공간('.')

r, c = map(int, input().split())
m = [list(map(str, input().split())) for i in range(r)]
zero = 0
one = 0
two = 0
three = 0
four = 0

# for row in m:
#     for element in row[0]:
#         print(element)
#     print()

for i in range(len(m)):
    for j in range(len(m[i][0])):
        try:
            if m[i][0][j] == '#' or m[i][0][j + 1] == '#' or m[i + 1][0][j] == '#' or m[i + 1][0][j + 1] == '#':
                continue
            count = 0
            if m[i][0][j] == 'X':
                count += 1
            if m[i][0][j + 1] == 'X':
                count += 1
            if m[i + 1][0][j] == 'X':
                count += 1
            if m[i + 1][0][j + 1] == 'X':
                count += 1

            if count == 0:
                zero += 1
            elif count == 1:
                one += 1
            elif count == 2:
                two += 1
            elif count == 3:
                three += 1
            elif count == 4:
                four += 1
        except:
            continue
print(zero)
print(one)
print(two)
print(three)
print(four)