def solution(k, score):
    answer = []
    hall = []
    for i in score:
        if len(hall) < k:
            hall.append(i)
            answer.append(min(hall))
        else:
            hall.append(i)
            hall.pop(hall.index(min(hall)))
            answer.append(min(hall))

    return answer