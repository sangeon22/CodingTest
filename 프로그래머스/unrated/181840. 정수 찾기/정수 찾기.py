def solution(num_list, n):
    # return 1 if num_list.count(n) > 0 else 0 
    try:
        num_list.index(n) > 0
    except:
        return 0
    return 1
