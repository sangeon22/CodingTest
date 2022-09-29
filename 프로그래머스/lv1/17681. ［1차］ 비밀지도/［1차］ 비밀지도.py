def solution(n, arr1, arr2):
    answer = []
    temp1 = []
    temp2 = []
    for i in range(n):
        temp1.append(arr1[i]|arr2[i])
    
    for i in temp1:
        temp2.append(str(bin(i)[2:]))
    
    for i in temp2:
        if len(i) == n:
            answer.append(i.replace("1", "#").replace("0"," "))
        else:
            zero_i = "0"*(n-len(i)) +i
            answer.append(zero_i.replace("1", "#").replace("0"," "))
    
    return answer

