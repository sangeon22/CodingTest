from collections import defaultdict

def solution(clothes):
    answer = 1
    
    # dic = {}
    # for item in clothes:
    #     key = hash(item[1])
    #     value = item[0]
    #     if key in dic:
    #         dic[key].append(value)
    #     else:
    #         dic[key] = [value]
    
    dic = defaultdict(list)
    for value, key in clothes:
        dic[key].append(value)

    for i in dic:
        answer *= (len(dic[i])+1)


    return answer - 1