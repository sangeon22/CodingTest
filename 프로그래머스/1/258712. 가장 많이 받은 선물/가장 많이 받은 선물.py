from itertools import combinations


def solution(friends, gifts):
    dic = {}
    giver_dic = {}
    taker_dic = {}
    answer_dic = {}

    for i in friends:
        answer_dic[i] = 0
        giver_dic[i] = 0
        taker_dic[i] = 0

    # {
    #   "muzi": {"muzi": 0, "ryan": 0, "frodo": 0, "neo": 0},
    #   "ryan": {"muzi": 0, "ryan": 0, "frodo": 0, "neo": 0},
    #   "frodo": {"muzi": 0, "ryan": 0, "frodo": 0, "neo": 0},
    #   "neo": {"muzi": 0, "ryan": 0, "frodo": 0, "neo": 0}
    # }
    # 상단 주석처럼 회원 별 다른 회원에게 선물한 갯수 초기화
    for friend in friends:
        dic[friend] = {}
        for i in friends:
            dic[friend][i] = 0

    # 회원 별로 선물한 사람 값에 += 1
    for i in gifts:
        giver, taker = i.split()
        dic[giver][taker] += 1
        giver_dic[giver] += 1
        taker_dic[taker] += 1

    # 다음 달에 선물을 주고 받을 사람 결정
    comb = list(combinations(friends, 2))
    for x, y in comb:
        x_count = dic[x][y]
        y_count = dic[y][x]

        if x_count > y_count:
            answer_dic[x] += 1
        elif y_count > x_count:
            answer_dic[y] += 1
        else:
            x_gift_point = giver_dic[x] - taker_dic[x]
            y_gift_point = giver_dic[y] - taker_dic[y]

            if x_gift_point > y_gift_point:
                answer_dic[x] += 1
            elif y_gift_point > x_gift_point:
                answer_dic[y] += 1

    # x_give = dic[x][y]
    # y_give = dic[y][x]
    #
    # # 2. 두 사람이 선물을 주고 받은 적 X거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람에게 선물 지수가 더 작은 사람이 다음 달 +=1
    # if (x_give == 0 and y_give == 0) or (x_give == y_give):
    #     #    2.2. 만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.
    #     x_gift_point = giver_dic[x] - taker_dic[x]
    #     y_gift_point = giver_dic[y] - taker_dic[y]
    #     if x_gift_point == y_gift_point:
    #         continue
    #     else:
    #         #    2.1. 만약 A와 B가 선물을 주고 받은 적 X거나 정확히 같은 수로 선물을 주고 받았다면, B가 A에게 다음 달 += 1
    #         answer_dic[y] += 1
    #
    # # 1. 두 사람이 선물을 주고 받은 적 O, 더 많은 선물을 준 사람에게 덜 준 사람이 다음 달 += 1
    # if x_give > 0 or y_give > 0:
    #     x_give_count = sum(value for value in dic[x].values())
    #     y_give_count = sum(value for value in dic[y].values())
    #
    #     if x_give_count > y_give_count:
    #         answer_dic[x] += 1
    #     elif x_give_count < y_give_count:
    #         answer_dic[y] += 1

    answer = max(answer_dic.values())

    return answer
