def solution(k, m, score):
    answer = 0
    box = len(score) // m

    score = sorted(score, reverse=True)[0: box * m]
    for i in range(0, box):
        answer += min(score[m * i:m * (i + 1)]) * m
    return answer