target = input()
n = int(input())
answer = 0

for i in range(n):
    r = input() * 2
    if target in r:
        answer += 1

print(answer)
