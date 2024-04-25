from itertools import permutations


def solution(numbers):
    answer = -1
    # 시간초과
    # perm = permutations(numbers, len(numbers))
    # for i in perm:
    #     target = int("".join(list(map(str, i))))
    #     if target > answer:
    #         answer = target
    str_numbers = list(map(str, numbers))

    # 각 숫자를 문자열로 변환한 후 3번 반복하여 정렬
    arr = sorted(str_numbers, key=lambda x: x * 3, reverse=True)

    return str(int("".join(arr)))


numbers = [6, 10, 2]
# 기댓값 〉	"6210"
print(solution(numbers))

