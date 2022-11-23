def solution(num, total):
    answer = []
    a = num // 2
    mid = total / num

    if total % num == 0:
        answer.append(mid)
        for i in range(1, a + 1):
            answer.append(int(mid) - i)
            answer.append(int(mid) + i)
    else:
        answer.append(int(mid))
        answer.append(int(mid) + 1)
        for i in range(1, a):
            answer.append(int(mid) - i)
            answer.append(int(mid) + i+1)

    answer.sort()
    return answer