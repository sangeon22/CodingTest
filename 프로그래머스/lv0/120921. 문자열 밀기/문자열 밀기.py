from collections import deque


def solution(A, B):
    answer = 0
    a = deque(list(A))

    while (True):
        if ''.join(i for i in a) == B:
            return answer
        elif answer == len(A):
            return -1
        else:
            a.rotate(1)
            answer += 1