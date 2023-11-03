def solution(num_list):
    # odd = sum(num_list[0::2])
    # even = sum(num_list[1::2])
    # return odd if even <= odd else even
    return max(sum(num_list[0::2]), sum(num_list[1::2]))