from itertools import permutations


def solution(k, dungeons):
    answer = 0
    temp = 0

    for i in permutations(dungeons):
        if temp > answer:
            answer = temp

        if answer == len(dungeons):
            return answer

        hp = k
        temp = 0
        for j in i:
            if hp >= j[0]:
                hp -= j[1]
                temp += 1

    return answer