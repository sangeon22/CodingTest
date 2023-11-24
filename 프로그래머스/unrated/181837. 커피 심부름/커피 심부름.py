def solution(o):
    answer = 0
    for i in o:
        if "cafelatte" in i:
            answer += 5000
        else:
            answer += 4500
    return answer