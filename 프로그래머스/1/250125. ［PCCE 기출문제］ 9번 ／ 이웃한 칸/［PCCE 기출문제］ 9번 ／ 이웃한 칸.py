def solution(board, h, w):
    answer = 0
    target = board[h][w]

    # 0인 경우, 존재X
    if h != 0:
        try:
            if board[h-1][w] == target:
                answer += 1
        except:
            pass

    # 0인 경우, 존재X
    if w != 0:
        try:
            if board[h][w - 1] == target:
                answer += 1
        except:
            pass
    
    # board 범위를 벗어나는 경우 exception 처리
    try:
        if board[h+1][w] == target:
            answer += 1
    except:
        pass

    try:
        if board[h][w+1] == target:
            answer += 1
    except:
        pass

    return answer