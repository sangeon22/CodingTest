# 맞긴 하지만 역시 시간초과.. product는 수가 좀만 커져도 엄청 느려진다
# from itertools import product
#
#
# def solution(n):
#     answer = 0
#     step = [1, 2]
#     # 2000이하 정수이니 완전탐색도 괜찮을듯
#     # 중복 순열 사용?
#     for i in range(1, n + 1):
#         comb = list(product(step, repeat=i))
#         # 합이 n 칸 이하 인것만 살리기
#         for j in comb:
#             if sum(j) == n:
#                 answer += 1
#
#     return answer % 1234567

from itertools import combinations


def solution(n):
    answer = 0
    # step = [1, 2]
    # # 1칸(1 * n개)으로만 구성
    # answer += 1
    #
    # # 2칸(2 * (n//2))으로만 구성 -> n % 2 == 0 일 경우에만 존재
    # if n % 2 == 0:
    #     answer += 1

    # 1칸, 2칸으로 구성
    # 경우의 수 그려보니 가설이 맞다면,
    # 1칸 -> [1] 1가지
    # 2칸 -> [1,1][2] 2가지
    # 3칸 -> [1,1,1][1,2][2,1] 3가지
    # 4칸 -> [1,1,1,1][1,1,2][1,2,1][2,1,1][2,2] 5가지
    # 5칸 -> [1,1,1,1,1][2,1,1,1][1,2,1,1][1,1,2,1][1,1,1,2][2,2,1][2,1,2][1,2,2] 8가지
    # 점화식.. dp
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n-1] % 1234567
