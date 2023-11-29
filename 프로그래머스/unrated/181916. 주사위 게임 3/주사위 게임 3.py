from collections import Counter

def solution(a, b, c, d):
    answer = 0
    dic = Counter([a, b, c, d]).most_common()
    
    if len(dic) == 1:
        return dic[0][0] * 1111
    elif len(dic) == 2:
        if dic[0][1] == 3:
            return (10 * dic[0][0] + dic[1][0]) ** 2
        return (dic[0][0] + dic[1][0]) * abs(dic[0][0] - dic[1][0])
    elif len(dic) == 3:
        return  dic[1][0] * dic[2][0]
    elif len(dic) == 4:
        return min(dic)[0]
    
    return dic
        
        
    return a