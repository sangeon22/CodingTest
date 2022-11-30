from itertools import permutations


def solution(k, dungeons):
    answer = 0
    temp = 0

    com = list(permutations(dungeons))
    for i in com:
        if temp > answer:
            answer = temp
        hp = k
        temp = 0
        for j in i:
            if hp >= j[0]:
                hp -= j[1]
                temp += 1
        if answer == len(dungeons):
            return answer

    return answer