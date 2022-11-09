from itertools import combinations
def solution(nums):
    half = len(nums)//2
    set_count = len(list(set(nums)))
    if set_count >= half:
        return half;
    elif set_count < half:
        return set_count
    
    
#     li = list(combinations(nums,half))
    
#     for i in li:
#         if i[0] != i[1]:
#             answer += 1
#             if list(reversed(i)) in li:
#                 set_count += 1
