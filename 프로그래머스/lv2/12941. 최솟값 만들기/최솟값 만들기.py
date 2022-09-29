from itertools import product

def solution(A,B):
    answer = 0
    A.sort(reverse = False)
    B.sort(reverse = True)
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer