def solution(clothes):
    dic = {}
    answer = 1

    for item in clothes:
        key = item[1]
        value = item[0]
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]

    for i in dic:
        answer *= (len(dic[i])+1)


    return answer - 1