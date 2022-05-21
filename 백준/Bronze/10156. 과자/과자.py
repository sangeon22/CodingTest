# 과자 1개 K원
# 과자 개수 N
# 개진 돈 M1
# 빌릴 돈 M2
# 필요한 돈 K*N

k, n, m1 = map(int, input().split())
m2 = (k*n) - m1

if(m2<0):
    print(0)
else:
    print(m2)

