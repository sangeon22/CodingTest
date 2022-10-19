from collections import deque
def solution(numbers, direction):
    answer = []
    li = deque(numbers)
    if direction == "right":
        li.rotate(1)
        answer = list(li)
    else:
        li.rotate(-1)
        answer = list(li)
                      
    return answer