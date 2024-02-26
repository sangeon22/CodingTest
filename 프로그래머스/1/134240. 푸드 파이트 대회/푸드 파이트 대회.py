def solution(food):
    answer = ''
    temp = ''
    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            temp += str(i)
    answer += temp
    answer += "0"
    answer += "".join(list(reversed(temp)))
    return answer