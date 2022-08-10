from sys import stdin

a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, stdin.readline().split())
result = ""

while N != 0:
    result += (a[N % B])
    N = N // B

print(result[::-1])