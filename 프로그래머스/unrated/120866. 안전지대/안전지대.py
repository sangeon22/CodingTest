def solution(board):
    target = []

    # 1 좌표 추출
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                target.append([i, j])

    # 1인 좌표 주변 1로 변경
    for i in target:
        fill_around(board, i)

    # 0인 좌표 개수 추출
    return sum(i.count(0) for i in board)


def fill_around(board, target):
    i, j = target
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < len(board) and 0 <= y < len(board):
                board[x][y] = 1