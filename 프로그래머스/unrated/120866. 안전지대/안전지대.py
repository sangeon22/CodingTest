def solution(board):
    answer = 0
    n = len(board)
    target = []

    # 0인 좌표 수 추출
    for i in board:
        for j in i:
            if j == 0:
                answer += 1
    if answer == 0:
        return 0

    # 1 좌표 추출
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                target.append([i, j])

    # 1인 좌표 주변 1로 변경
    for i in target:
        fill_around(board, i)

    # 0인 좌표 수 추출
    answer = 0  # 기존 answer 값을 초기화해야 함
    for i in board:
        for j in i:
            if j == 0:
                answer += 1
    return answer

def fill_around(board, target):
    i, j = target  # target을 좌표 [i, j]로 언팩
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                board[x][y] = 1