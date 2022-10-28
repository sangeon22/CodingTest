def solution(array, n):
    array.sort()
    li = [abs(n-i) for i in array]
    
    return array[li.index(min(li))]