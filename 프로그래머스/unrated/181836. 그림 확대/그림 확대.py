def solution(p, k):
    answer = []
    for i in p:
        temp = ""
        for j in i:
            temp += j*k
        for _ in range(k):
            answer.append(temp)
    return answer