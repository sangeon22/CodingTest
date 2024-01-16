from collections import deque

for _ in range(int(input())):
    n = int(input())
    card = list(map(ord, input().split()))
    answer = deque([card[0]])

    for i in range(1, len(card)):
        if answer[0] >= card[i]:
            answer.appendleft(card[i])
        else:
            answer.append(card[i])

    print(''.join(map(chr, answer)))
