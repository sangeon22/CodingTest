def solution(quiz):
    answer = []
    for i in quiz:
        li = i.split("=")
        answer.append("O" if eval(li[0]) == int(li[1]) else "X")

    return answer