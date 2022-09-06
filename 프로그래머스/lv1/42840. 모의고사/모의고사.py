def solution(answers):
    answer = []
    st1 = [1,2,3,4,5]
    st2 = [2,1,2,3,2,4,2,5]
    st3 = [3,3,1,1,2,2,4,4,5,5]
    count1=0
    count2=0
    count3=0
    
    for i in range(len(answers)):
        if answers[i] == st1[i%5]:
            count1+=1
        if answers[i] == st2[i%8]:
            count2+=1
        if answers[i] == st3[i%10]:
            count3+=1
            
    countlist = [count1,count2,count3]
    maxcount = max(countlist)
    
    for i in range(len(countlist)):
        if countlist[i] == maxcount:
            answer.append(i+1)
    return answer