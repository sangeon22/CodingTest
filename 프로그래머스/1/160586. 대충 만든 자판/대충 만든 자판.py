def solution(keymap, targets):
    answer = []
    for i in targets:
        count = 0
        for j in range(len(i)):
            idx = min(list(map(lambda x: x.index(i[j]) + 1 if i[j] in x else 102, keymap)))
            if idx >= 102:
                answer.append(-1)
                break

            count += idx

            if j == len(i) - 1:
                answer.append(count)
    return answer

