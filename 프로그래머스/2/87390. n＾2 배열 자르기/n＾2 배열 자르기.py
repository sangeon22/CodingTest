def solution(n, left, right):
    # 시도 1) 테스트 케이스는는 맞지만 히든 수가 너무 커서 케이스에서 시간 초과
    # arr = [[0 for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         arr[i][j] = max(i, j) + 1
    #
    # return sum(arr, [])[left:right + 1]

    # 시도 2) 테스트 케이스는는 맞지만 히든 수가 너무 커서 케이스에서 시간 초과
    # 그러나 수가 거대해지니 시간초과.. 리스트를 만들때 너무 큰 듯
    # n = 10 일 때, 일정한 패턴을 발견
    # 각 행은 i~n까지 존재 i는 그 행의 수만큼 존재(i만큼 존재) -> 2중 반복 안해도 됨 n**2 X
    # [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 3, 3, 4, 5, 6, 7, 8, 9, 10],
    #  [4, 4, 4, 4, 5, 6, 7, 8, 9, 10], [5, 5, 5, 5, 5, 6, 7, 8, 9, 10], [6, 6, 6, 6, 6, 6, 7, 8, 9, 10],
    #  [7, 7, 7, 7, 7, 7, 7, 8, 9, 10], [8, 8, 8, 8, 8, 8, 8, 8, 9, 10], [9, 9, 9, 9, 9, 9, 9, 9, 9, 10],
    #  [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
    # answer = ""
    # answer2 = ""
    # num = "".join([str(i) for i in range(1, n + 1)])
    # for i in range(1, n + 1):
    #     answer2 += str(i) * i + num[i:n + 1]
    # a = list(map(int, answer2[left:right + 1]))

    # 시도 3)
    # 필요한 구간만 구함
    #  left // n 배열 구간부터 right // n 구간까지만 구하면 됨
    # answer = ""
    # num = "".join([str(i) for i in range(1, n + 1)])
    # for i in range(left // n + 1, right // n + 2):
    #     answer += str(i) * i + num[i:n + 1]
    # if left // n > 0:
    #     d = right - left
    #     left %= n
    #     right = left + d
    #
    # answer = list(map(int, answer[left: right + 1]))

    answer = []
    for i in range(left, right + 1):
        # 행 열 계산
        answer.append(max(i // n, i % n) + 1)
    return answer