def solution(s):
    answer = ''
    li = []
    for i in s:
        li.append(ord(i))
        
    li.sort(reverse = True)
    for i in li:
        answer += chr(i)
    
    return answer