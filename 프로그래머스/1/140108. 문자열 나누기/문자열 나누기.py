def solution(s):
    answer = []
    count = [0, 0]
    temp = ""
    x = ""

    for i in range(len(s)):
        if temp == "":
            x = s[i]
        
        temp += s[i]

        if s[i] == x:
            count[0] += 1
        else:
            count[1] += 1

        if count[0] == count[1] or i == len(s) -1:
            answer.append(temp)
            temp = ""

    return len(answer)