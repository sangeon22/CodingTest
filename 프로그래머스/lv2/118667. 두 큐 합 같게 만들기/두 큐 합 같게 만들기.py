from collections import deque


def solution(queue1, queue2):
    li1 = deque(queue1)
    li2 = deque(queue2)
    target = (sum(li1) + sum(li2)) / 2
    li1_sum = sum(li1)

    if target % 1 != 0:
        return -1

    count = 0
    # while li1 and li2:
    for i in range(0, 300000):
        if li1_sum > target:
            temp = li1.popleft()
            li1_sum -= temp
            li2.append(temp)
        elif li1_sum < target:
            temp = li2.popleft()
            li1_sum += temp
            li1.append(temp)
        else:
            return i

    return -1