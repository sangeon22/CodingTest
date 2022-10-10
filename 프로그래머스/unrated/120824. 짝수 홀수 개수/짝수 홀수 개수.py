def solution(num_list):
    answer = []
    
    temp = [ i for i in num_list if i % 2 == 0 ]
    answer.append(len(temp))
    
    temp = [ i for i in num_list if i % 2 != 0 ]
    answer.append(len(temp))
    return answer