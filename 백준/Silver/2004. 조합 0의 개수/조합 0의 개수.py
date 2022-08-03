from sys import stdin


def five(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer


def two(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer


n, m = map(int, stdin.readline().split())

print(min(two(n) - two(m) - two(n - m), five(n) - five(m) - five(n - m)))