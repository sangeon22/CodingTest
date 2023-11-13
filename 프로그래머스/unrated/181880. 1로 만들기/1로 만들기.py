def solution(n):
    answer = 0
    for i in n:
        while i != 1:
            if i % 2 == 0:
                answer += 1
                i /= 2
            else:
                i -= 1
    return answer