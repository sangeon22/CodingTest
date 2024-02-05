def solution(name, yearning, photo):
    answer = []

    for i in photo:
        total = 0
        for j in i:
            if j in name:
                total += yearning[name.index(j)]
        answer.append(total)

    return answer