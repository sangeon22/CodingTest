def solution(s):
    li = []
    
    for i in range(len(s)):
        if len(li) == 0:
            li.append(s[i])
        else:
            if s[i] == li[-1]:
                li.pop()
            else:
                li.append(s[i])
                
    if len(li) == 0:
        return 1
    else:
        return 0