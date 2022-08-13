from sys import stdin

# A진법 -> 10진법 -> B진법
A, B = map(int, stdin.readline().split(" "))
m = int(stdin.readline())

li = list(map(int, stdin.readline().split(" ")))
result = []
s = 0
total = 0

for i in li[::-1]:
    total += i * pow(A, s)
    s += 1

while total:
    result.append(str(total % B))
    total = total // B

result.reverse()
print(*result)