def solution(common):
#     a1 = common[0]
    
#     if (common[1] - common[0]) == (common[2] - common[1]):
#         d = common[1] - common[0]
#         return a1 + len(common)*d
#     else:
#         r = common[1] - common[0]
#         return a1 * r **len(common)

    if (common[1] - common[0]) == (common[2] - common[1]):
        return common[-1] + common[1] - common[0]
    else:
        return common[-1] * (common[1] / common[0])


                