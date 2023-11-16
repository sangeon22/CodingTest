def solution(s):
    answer = []
    s = s[:-2].replace('{','').replace(',',' ').split('}')
    s = [i.split() for i in s]
    s.sort(key=lambda x:len(x))
    
    for i in s:
        a = set(i) - set(answer)
        answer.append(list(a)[0])
    return list(map(int, answer))