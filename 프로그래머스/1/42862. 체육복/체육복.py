def solution(n, lost, reserve):
#     lost_set = set(lost) - set(reserve)
#     reserve_set = set(reserve) - set(lost)

#     for i in reserve_set:
#         if i - 1 in lost_set:
#                 lost_set.remove(i - 1)
#         elif i + 1 in lost_set:
#                 lost_set.remove(i + 1)
#     return n - len(lost_set)

    lost_set= list(set(lost) - set(reserve))
    reserve_set = list(set(reserve) - set(lost))
    
    for i in reserve_set[:]:
        if i - 1 in lost_set:
            lost_set.remove(i-1)
        elif i + 1 in lost_set:
            lost_set.remove(i+1)
    return n - len(lost_set)