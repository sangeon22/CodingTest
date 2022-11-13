def solution(sides):
    answer = 0
# 가장 긴 변이 배열안에 존재하는 경우
    for i in range(1, max(sides)+1):
        if i + min(sides) > max(sides):
            answer += 1

# 나머지 한 변이 가장 긴 변인 경우
    for i in range(max(sides)+1, sum(sides)):
        answer += 1
    return answer