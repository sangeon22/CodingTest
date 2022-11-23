def solution(num, total):
    answer = []
    a = num // 2
    mid = int(total / num)
    answer.append(mid)

    if total % num == 0:
        for i in range(1, a + 1):
            answer.append(mid - i)
            answer.append(mid + i)
    else:
        answer.append(mid + 1)
        for i in range(1, a):
            answer.append(mid - i)
            answer.append(mid + 1 + i)

    answer.sort()
    return answer