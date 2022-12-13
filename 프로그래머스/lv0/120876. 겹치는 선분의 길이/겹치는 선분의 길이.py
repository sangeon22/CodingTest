def solution(lines):
    line = []
    common = []
    answer = 0

    for i in lines:
        temp = []
        for j in range(i[0], i[1] + 1):
            temp.append(j)
        line.append(temp)

    common.append(list(set(line[0]) & set(line[1])))
    common.append(list(set(line[0]) & set(line[2])))
    common.append(list(set(line[1]) & set(line[2])))

    for i in range(len(common)):
        if len(common[i]) == 1:
            common[i].clear()
        if common[i]:
            answer += max(common[i]) - min(common[i])

    if common[0] and common[1] and common[2]:
        li1 = set(common[0]) & set(common[1])
        li2 = set(common[1]) & set(common[2])
        answer -= max(li1) - min(li1)
        answer -= max(li2) - min(li2)

    return answer