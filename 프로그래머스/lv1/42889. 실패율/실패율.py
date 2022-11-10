def solution(N, stages):
    answer = []
    dic = {}

    for i in range(1, N + 1):
        dic[i] = 0

    stages.sort()
    set_stages = set(stages)

    for i in set_stages:
        if stages.count(i) > 0:
            dic[i] = stages.count(i) / len(stages)
            while i in stages:
                stages.remove(i)

    for i in sorted(dic.items(), key=lambda x: x[1], reverse=True):
        if i[0] != N+1:
            answer.append(i[0])

    return answer