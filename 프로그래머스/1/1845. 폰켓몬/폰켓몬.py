def solution(nums):
    answer = 0
    return min(len(list(set(nums))), len(nums)//2)