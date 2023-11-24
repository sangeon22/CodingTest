from collections import Counter


def solution(s):
    answer = [0] * 52
    li = [[ord(i)-65, j] if ord(i) <= 90 else [ord(i)-71, j] for i, j in Counter(s).most_common()]
    for i in li:
        answer[i[0]] = i[1]
    return answer