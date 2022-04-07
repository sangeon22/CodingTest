h, m = map(int, input().split())
t = int(input())

total_m = m + t
total_h = h

if total_m >= 60:
    h1 = total_m // 60
    total_m %= 60
    total_h = h1 + h

if total_h >= 24:
    total_h %= 24

print(total_h, total_m, end=" ")
