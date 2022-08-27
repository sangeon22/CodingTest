def solution(s):
    answer = ''
    count = ((len(s))//2)
    if len(s) % 2 == 0:
        answer = s[count-1]+s[count]  
        
    else:
        answer = s[count]  
    
    return answer