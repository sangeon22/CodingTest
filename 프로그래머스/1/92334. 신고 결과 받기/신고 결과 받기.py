from collections import Counter

def solution(id_list, report, k):
    answer = []
    dic = {}

    # dict 선언, 값은 set으로 중복 제거(같은 유저라면 다중신고를 1건으로 처리)
    for user_id in id_list:
        dic[user_id] = set()

    # 각 유저가 신고한 대상을 딕셔너리에 저장
    for i in report:
        reporter, target = i.split()
        dic[reporter].add(target)

    # 각 유저 별 신고 당한 횟수 체크
    count = Counter(reporter for reporters in dic.values() for reporter in reporters)

    # 각 id 별 정지 대상자 발송 횟수
    for i in dic:
        cnt = 0
        for j in dic[i]:
            if count[j] >= k:
                cnt += 1
        answer.append(cnt)

    return answer
