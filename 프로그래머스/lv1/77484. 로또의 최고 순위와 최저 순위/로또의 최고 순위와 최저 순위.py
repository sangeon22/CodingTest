def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    total = 0
    zero = lottos.count(0)

    for i in lottos:
        if i in win_nums:
            total += 1

    print(zero+total)
    answer.append(rank[zero + total])
    answer.append(rank[total])

    return answer