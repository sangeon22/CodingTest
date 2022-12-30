from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    wait = deque(people.copy())

    while wait:
        if len(wait) > 1:
            if wait[0] + wait[-1] <= limit:
                wait.popleft()
                wait.pop()
                answer += 1
            elif wait[0] + wait[-1] > limit:
                wait.pop()
                answer += 1
        else:
            wait.pop()
            answer += 1

    # wait = people.copy()
    # for i in range(len(people)):
    #     total = 0
    #     if wait:
    #         if people[i] < limit:
    #             answer += 1
    #             total += people[i]
    #             wait.remove(people[i])
    #             while True:
    #                 if limit - people[i] >= total in wait:
    #                     total += wait[0]
    #                     wait.remove(wait[0])
    #                 else:
    #                     break
    #
    #         elif people[i] == limit:
    #             answer += 1
    #             wait.remove(people[i])
    #     else:
    #         break

    return answer