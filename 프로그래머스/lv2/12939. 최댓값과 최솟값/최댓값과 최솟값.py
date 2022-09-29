def solution(s):
    answer = ''
    temp = map(int, s.split(" "))
    li = list(temp)
    answer += str(min(li))
    answer += " "
    answer += str(max(li))
    
    
    
    return answer