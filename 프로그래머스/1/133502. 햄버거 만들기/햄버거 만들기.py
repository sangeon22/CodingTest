def solution(ingredient):
    answer = 0
    arr = []
    for i in range(len(ingredient)):
        arr.append(ingredient[i])
        if ingredient[i] == 1 and len(arr) > 3:
            idx_count = 4 * answer
            if arr[i - idx_count - 3] == 1 and arr[i - idx_count - 2] == 2 and arr[i - idx_count - 1] == 3:
                del (arr[i - idx_count - 3: i - idx_count + 1])
                answer += 1

    return answer


# 1. 스택으로 계속 쌓고 1,2,3,1이면 pop 후 answer += 1 -> 1,000,000 최대 길이이므로 시간초과 뜰 거 같음

# 2. 문자열로 넣어도 그런가? -> test Case 통과하긴 하는데 역시 히든케이스에서 시간초과
#     temp = ""
# 
#     for i in ingredient:
#         temp += str(i)
#         if "1231" in temp:
#             answer += 1
#             temp = temp.replace("1231","")
# 문자열이든 스택이든 순차탐색하는 방법은 좋지 않은 듯

# 3. 그냥 ingredient를 한번에 문자열로 만들고 replace 횟수 체크? -> testCase 통과하긴 하는데 히든 케이스 18개 중 4개 시간초과 -> 성능 개선 필요? 아니면 다른 알고리즘
# answer = 0
# str_ingredient = "".join(map(str, ingredient))
# while True:
#     replace_ingredient = str_ingredient.replace("1231", "", 1)
#
#     if len(str_ingredient) == len(replace_ingredient):
#         return answer
#
#     str_ingredient = replace_ingredient
#     answer += 1
# replace도 역시 완전 탐색으로 시간이 너무 오래 걸림

# 4. 1번 방법인데 재정렬안하고 제거하는 방법? del
