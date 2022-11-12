def solution(s):
    answer = []
    li = []
    
    s = s[2:-2].split("},{")

    for i in s:
        li.append(list(map(int, i.split(','))))

    
    li.sort(key=len)
    
    dic = {i:0 for i in li[-1]}
    
    for i in li[-1]:
        temp = 0
        for j in li:
            temp += j.count(i)
        dic[i] = temp
    
    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse =True)
    
    for i in range(len(sorted_dic)):
        answer.append(sorted_dic[i][0])
        
    return answer