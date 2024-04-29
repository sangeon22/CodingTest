from collections import Counter

def solution(topping):
    answer = 0
    # 1 ≤ topping의 길이 ≤ 1,000,000
    # 토핑의 길이 최대 값이 너무 커서 완전 탐색은 시간초과 뜰 것 같음 -> 히든케이스에서 시간초과 뜸 (2/20 통과)
    # for i in range(len(topping) - 1):
    #     x = set(topping[:i + 1])
    #     y = set(topping[i + 1:])
    #     a = len(x)
    #     b = len(y)
    #     if a == b:
    #         answer += 1

    # a한테 토핑을 전부 몰아주고 각 토핑 별, 갯수 체크
    a = Counter(topping)
    b = set()

    # 토핑 하나씩 꺼내면서
    for i in topping:

        # a한테 해당 토핑 갯수 -1
        # b한테 해당 토핑 추가
        a[i] -= 1
        b.add(i)
        # 해당 토핑에 값이 없으면 제거
        if a[i] < 1:
            a.pop(i)

        if len(a) == len(b):
            answer += 1

    return answer
