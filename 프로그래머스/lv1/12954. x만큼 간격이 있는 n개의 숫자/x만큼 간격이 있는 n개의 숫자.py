def solution(x, n):
    answer = []
    while n != 0:
        answer.append(x*n)
        n -= 1

    answer.reverse()
    return answer