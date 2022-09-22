def solution(x):
    li = list(map(int, str(x)))
    total = sum(li)
    
#     total = 0

#     for i in li:
#         total += i
        
    if x % total == 0:
        return True
    
    return False