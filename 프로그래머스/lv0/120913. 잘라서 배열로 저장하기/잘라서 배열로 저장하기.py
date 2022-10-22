def solution(my_str, n):
    answer = []
    # print(my_str[0:n])
    # print(my_str[n:n*2])
    # print(my_str[n*2:n*3])
    for i in range(len(my_str)//n+1):
        if my_str[n*i:n*(i+1)] != "":
            answer.append(my_str[n*i:n*(i+1)])
        
    return answer