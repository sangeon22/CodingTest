def solution(participant, completion):
    dic = {}
    temp = 0
    for i in participant:
        dic[hash(i)] = i
        temp += hash(i)
        
    for i in completion:
        temp -= hash(i)
        
    return dic[temp]