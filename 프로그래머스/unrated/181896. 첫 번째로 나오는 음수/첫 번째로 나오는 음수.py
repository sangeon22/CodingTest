def solution(num_list):
    for i in num_list:
        if i < 0:
            return num_list.index(i)
    return -1 