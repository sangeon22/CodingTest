import math

def solution(num_list):
    return 1 if math.prod(num_list) < sum(num_list) ** 2 else 0