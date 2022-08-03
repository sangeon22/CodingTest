from sys import stdin


def f(x, y):
    answer = 0
    while x != 0:
        x = x // y
        answer += x
    return answer


a, b = map(int, stdin.readline().split())

print(min(f(a, 2) - f(a - b, 2) - f(b, 2), f(a, 5) - f(a - b, 5) - f(b, 5)))


# def five(n):
#     answer = 0
#     while n != 0:
#         n = n // 5
#         answer += n
#     return answer
# 
# 
# def two(n):
#     answer = 0
#     while n != 0:
#         n = n // 2
#         answer += n
#     return answer
# 
# 
# n, m = map(int, stdin.readline().split())
# 
# print(min(two(n) - two(m) - two(n - m), five(n) - five(m) - five(n - m)))