def solution(str):
    a = 0
    if str.startswith('0'):
        for i in str:
            if i != '0':
                a = str.index(i)
                break
        return str[a:] 
    else:
        return str
        