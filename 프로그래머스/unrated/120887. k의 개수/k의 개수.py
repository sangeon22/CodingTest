def solution(i, j, k):
    answer = 0
    li = [str(i) for i in range(i, j+1)]
    answer = ''.join(li).count(str(k))
    return answer
    