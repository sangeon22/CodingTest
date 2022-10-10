def solution(array, height):
    answer = 0
    array.append(height)
    array.sort(reverse = True)
    for i in array:
        if i == height:
            return answer
        answer += 1