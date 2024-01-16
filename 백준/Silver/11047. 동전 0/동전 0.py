n, k = map(int, input().split())
money = [int(input()) for i in range(n)]
answer = 0
for i in money[::-1]:
    answer += k // i
    k %= i

print(answer)