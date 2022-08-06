from sys import stdin

n = stdin.readline()
n = int(n, 8)

print(bin(n)[2:])
