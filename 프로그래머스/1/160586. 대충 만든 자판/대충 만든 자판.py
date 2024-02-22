def solution(keymap, targets):
    answer = []

    for i in targets:
        count = 0
        for j in range(len(i)):
            # keymap의 각 요소에 target의 문자가 어느 인덱스에 위치하는지 찾음
            # 없으면 102(keymap 최대 길이가 100이니까)
            idx = min(list(map(lambda x: x.index(i[j]) + 1 if i[j] in x else 102, keymap)))
            if idx >= 102:
                answer.append(-1)
                break
                
            count += idx
            
            if j == len(i) - 1:
                answer.append(count)
    return answer

