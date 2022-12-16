# 첫시도 - int 재귀로 범위 초과 런타임에러
# def solution(n):
#     return f(n) % 1234567


# def f(num):
#     return f(num - 1) + f(num - 2)

def solution(n):
    answer = [0,1]
    [answer.append(answer[i-1] + answer[i-2]) for i in range(2, n+1)]
        
    return answer[-1] % 1234567