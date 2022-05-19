# I-1 < M/A < I
# = A(I-1) < M < AI
# 최소값이 A(I-1)이다.
A, I = map(int, input().split())
M = A * (I - 1) + 1
print(M)
