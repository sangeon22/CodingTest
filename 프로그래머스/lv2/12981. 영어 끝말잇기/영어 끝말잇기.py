import math
def solution(n, words):
    answer = []
    temp = []
    count = 0
    for i in words:
        count += 1
        
        if not temp:
            temp.append(i)
            continue

        if temp[-1][-1] != i[0] or i in temp:
            if count % n == 0:
                answer.append(n)
            else:
                answer.append(count % n)
            answer.append(math.ceil(count / n))
            break
        else:
            temp.append(i)

    if not answer:
        answer = [0, 0]

    return answer