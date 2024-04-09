import math


def solution(str1, str2):
    answer = 0
    top = 0
    bottom = 0

    # 대소문자 구분 없으니 모두 대문자로 변환
    str1 = str1.upper()
    str2 = str2.upper()

    # str1, str2 각각 조합 리스트
    arr1 = []
    arr2 = []

    # str1로 만든 조합 리스트 arr1 => 문자 값만 조합 구성
    pre_str = str1[0]
    for i in range(1, len(str1)):
        if (pre_str + str1[i]).isalpha():
            arr1.append(pre_str + str1[i])
        pre_str = str1[i]

    # str2로 만든 조합 리스트 arr2 => 문자 값만 조합 구성
    pre_str = str2[0]
    for i in range(1, len(str2)):
        if (pre_str + str2[i]).isalpha():
            arr2.append(pre_str + str2[i])
        pre_str = str2[i]

    # 합집합
    union_set = set(arr1).union(arr2)

    # 교집합
    intersection_set = set(arr1).intersection(arr2)

    # 합집합 내 요소를 하나씩 순회하며, arr1과 arr2에서의 중복 갯수 파악 => 분모 갯수
    for i in union_set:
        arr1_count = arr1.count(i)
        arr2_count = arr2.count(i)
        bottom += max(arr1_count, arr2_count)

    # 교집합 내 요소를 하나씩 순회하며, arr1과 arr2에서의 중복 갯수 파악 => 분자 갯수
    for i in intersection_set:
        arr1_count = arr1.count(i)
        arr2_count = arr2.count(i)
        top += min(arr1_count, arr2_count)

    # ['FR', 'RA', 'AN', 'NC', 'CE']
    # ['FR', 'RE', 'EN', 'NC', 'CH']
    # 교집합 = [FR, NC]
    # 합집합 = [FR, RA, AN, NC, CE, RE, EN, CH]

    # 문제 조건에 의한 정답 계산
    # str1, str2 모두 공집합 일 경우, return 1 -> 65536
    try:
        answer = math.floor(65536 * (top / bottom))
    except:
        return 65536
    return answer
