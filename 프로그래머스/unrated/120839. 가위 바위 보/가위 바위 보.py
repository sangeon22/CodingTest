def solution(rsp):
    answer = ''
    # 2 0
    # 0 5
    # 5 2
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        elif i == '5':
            answer += '2'
        
    return answer