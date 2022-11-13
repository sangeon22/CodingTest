from collections import deque


def solution(A, B):
    
#     첫 성공 코드
#     answer = 0
#     a = deque(list(A))

#     while (True):
#         if ''.join(i for i in a) == B:
#             return answer
#         elif answer == len(A):
#             return -1
#         else:
#             a.rotate(1)
#             answer += 1

# 코드 리팩토링
    a = deque(A)
    b = deque(B)

    for i in range(len(A)):
        if a == b:
            return i
        else:
            a.rotate(1)
            
    return -1
            