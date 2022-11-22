def solution(s):
    s = s.split(" ")
    li = []
    
    if s[0] != 'Z':
        li.append(int(s[0]))

    for i in range(1, len(s)):
        if s[i] == 'Z':
            li.pop()   
        else:
            li.append(int(s[i]))
    
    return sum(li)