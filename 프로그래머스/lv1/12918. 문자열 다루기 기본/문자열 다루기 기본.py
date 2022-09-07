def solution(s):
    answer = False

    if (len(s) == 4 or len(s) == 6) and s.isdigit() == True:
        answer = True

    return answer