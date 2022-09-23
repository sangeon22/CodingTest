def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return f"김서방은 {i}에 있다"