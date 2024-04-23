def solution(elements):
    answer = []

    # 1 ~ len(elements)의 수 만큼 조합?을 구함
    # 각 원소를 시작 기준으로 위의 수 만큼 합을 구힘
    for i in range(1, len(elements) + 1):
        # 1개로 구성된 연속 부분 수열의 합은 중복 제거한 값 반환
        if i == 1:
            answer.extend(set(elements))
            continue

        # 연속 수열의 길이와 같은 경우, 각 요소의 합을 반환
        if i == len(elements):
            answer.append(sum(elements))
            continue

        # elements 요소를 다 순회하며, i 길이만큼 홥 추출
        temp = []
        for j in range(len(elements)):
            # elements의 길이를 벗어 나는 경우, 남은 길이만큼 슬라이싱
            if j + i > len(elements):
                temp.append(sum(elements[j:] + elements[:i-len(elements[j:])]))
                continue
            temp.append(sum(elements[j:j + i]))

        # 연속 수열의 합 저장
        answer.extend(temp)

    return len(set(answer))


elements = [7, 9, 1, 1, 4]
print(solution(elements))
