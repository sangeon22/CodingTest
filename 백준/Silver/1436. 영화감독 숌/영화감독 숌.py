from sys import stdin

n = int(stdin.readline())
s = 666

while True:
    if '666' in str(s):
        n -= 1
        if n == 0:
            break
    s = s + 1

print(s)