from collections import deque


def solution(numbers):
    # answer = []
    # deq = deque(numbers)
    # copy_numbers = deq.copy()

    # 첫번째 방법 시간 초과(23개 히든 케이스 중 15개가 시간초과)
    # # xxxx 4 ≤ numbers의 길이 ≤ 1,000,000 이므로, 정렬 및 탐색에 시간 초과가 뜰 것 같지만 일단 무지성 풀이 도전
    # # 위 방법으로 하려다 오래 걸릴거 같아서 deque로 변환해서 하나씩 popleft로 빼면 될 것 같음

    # for i in deq:
    #     num = i
    #     copy_numbers.popleft()
    #
    #     if copy_numbers:
    #         # 뒷큰수 존재X
    #         if num >= max(copy_numbers):
    #             answer.append(-1)
    #             continue
    #
    #         # 뒷큰수 존재O
    #
    #         # numbers 길이가 엄청 크면, 아래 필터링에서 오래 걸림
    #         # 현재 num 뒤에 있는 요소이면서 num 보다 큰 요소 필터링 후 가장 가까운 값 추출
    #         # arr = list(filter(lambda x: x > num, copy_numbers))
    #         # if arr:
    #         #     answer.append(arr[0])
    #
    #         next_larger_num = next(filter(lambda x: x > num, copy_numbers), -1)
    #         answer.append(next_larger_num)
    #
    #     # 마지막 index의 경우 -1
    #     else:
    #         answer.append(-1)

    # 두번째 방법 시간 초과(23개 히든 케이스 중 10개가 시간초과)
    # answer = []
    # deq = deque(numbers)
    # copy_numbers = deq.copy()
    # for _ in range(len(deq)):
    #     num = copy_numbers.popleft()
    #
    #     # 마지막 요소의 경우 -1
    #     if not copy_numbers:
    #         answer.append(-1)
    #         break
    #
    #     larger_num = -1
    #     # 뒷큰수 추출
    #     for j in range(len(copy_numbers)):
    #         next_num = copy_numbers[j]
    #         if next_num > num:
    #             larger_num = next_num
    #             answer.append(larger_num)
    #             break
    #
    #     # 뒷큰수 X
    #     if larger_num == -1:
    #         answer.append(-1)

    # 세번째 방법 시간 초과(23개 히든 케이스 중 4개가 시간초과)
    # answer = []
    # deq = deque(numbers)
    #
    # for _ in range(len(deq)):
    #     num = deq.popleft()
    #
    #     # 마지막 요소의 경우 -1
    #     if not deq:
    #         answer.append(-1)
    #         break
    #
    #     larger_num = -1
    #     # 뒷큰수 추출
    #     for next_num in deq:
    #         if next_num > num:
    #             larger_num = next_num
    #             break
    #
    #     if larger_num != -1:
    #         answer.append(larger_num)
    #     else:
    #         # 덱에서 현재 숫자보다 큰 수가 없으면 가장 가까운 큰 수는 덱의 맨 처음 값
    #         answer.append(-1)

    answer = []
    deq = deque(numbers)

    stack = []

    for num in reversed(deq):
        # 스택이 비어있지 않고 현재 숫자보다 작은 수가 스택에 있다면 해당 숫자를 pop
        while stack and stack[-1] <= num:
            stack.pop()

        # 스택이 비어있지 않으면, 현재 숫자보다 큰 수 중에서 가장 작은 수가 스택에 남아있음
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)

        # 현재 숫자를 스택에 추가
        stack.append(num)

    # 순서를 뒤집어 반환
    return answer[::-1]


# numbers = [2, 3, 3, 5]
# [3, 5, 5, -1]

numbers = [9, 1, 5, 3, 6, 2]
# 기댓값 〉	[-1, 5, 6, 6, -1, -1]
print(solution(numbers))
