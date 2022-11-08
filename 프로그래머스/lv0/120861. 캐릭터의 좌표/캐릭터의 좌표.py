def solution(keyinput, board):
    answer = [0, 0]
    width = [-(board[0]//2), board[0]//2]
    height = [-(board[1]//2), board[1]//2]
    
    for i in keyinput:
        if i == "left" and answer[0] > width[0]:
            answer[0] -= 1
        elif i == "right" and answer[0] < width[1]:
            answer[0] += 1
        elif i == "up" and answer[1] < height[1]:
            answer[1] += 1
        elif i == "down" and answer[1] > height[0]:
            answer[1] -= 1

    return answer