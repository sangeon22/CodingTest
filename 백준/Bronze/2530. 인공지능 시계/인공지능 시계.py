# 처음풀이
h, m, s = map(int, input().split())
d = int(input())

m1 = (s + d) // 60
s = (s + d) % 60

m += m1

if m >= 60:
    h1 = m // 60
    h += h1
    m %= 60

if h >= 24:
    h %= 24
print(h, m, s)

# 더 쉽게 풀이
h,m,s = map(int,input().split())
d = int(input())

s += d
m += s//60
h += m//60
print(h%24,m%60,s%60)
