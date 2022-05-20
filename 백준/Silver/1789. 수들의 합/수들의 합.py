# 1+2+3+4+5+6+7 ... N

s = int(input())
temp = 0

for i in range(1, s + 1):
    temp += i
    if s == 1:
        print(1)

    elif temp == s:
        print(i)
        break

    elif temp > s:
        print(i - 1)
        break
