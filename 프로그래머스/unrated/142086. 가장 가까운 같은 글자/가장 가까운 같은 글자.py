def solution(s):
    answer = []
    dic = {}

    for idx, i in enumerate(s):
        if i not in dic:
            answer.append(-1)
        else:
            answer.append(abs(dic[i] - idx))

        dic[i] = idx
        
    # 첫 시도는 테스트케이스는 통과하지만 히든케이스에서 실패
    # pre = []
    # count = 0
    # 
    # for i in range(len(s)):
    #     if s[i] not in pre:
    #         answer.append(-1)
    #     else:
    #         answer.append(abs(pre.index(s[i]) - i) - count)
    # 
    #     if s[i] in pre:
    #         pre.remove(s[i])
    #         count += 1
    # 
    #     pre.append(s[i])


    return answer