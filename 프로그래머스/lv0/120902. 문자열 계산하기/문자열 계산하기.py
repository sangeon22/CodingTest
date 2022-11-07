def solution(my_string):
    answer = 0
    li = my_string.split()
    temp = 0
    oper = ''
    for i in li:
        if i.isdigit():
            if oper == '-':
                answer -= int(i)
            else:
                answer += int(i)
        else:
            oper = i
            
    
    return answer