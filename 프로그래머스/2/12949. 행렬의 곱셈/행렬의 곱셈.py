import numpy

def solution(arr1, arr2):
    return numpy.dot(numpy.array(arr1), numpy.array(arr2)).tolist()


arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
# 기댓 값 [[15, 15], [15, 15], [15, 15]]

print(solution(arr1, arr2))
