def calc_date(today, date, month):
    date = date.split(".")

    # 개인정보 별 날짜 추출
    date_year = int(date[0])
    date_month = int(date[1])
    date_day = int(date[2])

    # 약관 날짜에 해당하는 개월 수를 개인 정보 별 날짜에 더함
    date_month += month
    # 유효기간은 해당 날짜에서 하루 빼야하니 조정
    if date_month > 12:
        date_year += date_month // 12
        date_month -= date_month // 12 * 12
        if date_month == 0:
            date_month = 12
            date_year -= 1

    if date_day == 1:
        date_day = 28
        date_month -= 1
        if date_month == 0:
            date_month = 12
            date_year -= 1
    else:
        date_day -= 1

    # 개인정보별 유효기간
    print(f"{date_year}.{date_month}.{date_day}")

    item = today.split(".")
    today_year = int(item[0])
    today_month = int(item[1])
    today_day = int(item[2])

    # today를 지난 개인정보 유효기간이면 True(폐기 대상)
    if today_year > date_year:
        return True
    elif today_year == date_year:
        if today_month > date_month:
            return True
        elif today_month == date_month:
            if today_day > date_day:
                return True
    return False


def solution(today, terms, privacies):
    answer = []

    # terms dict로 변경
    dic = dict()
    for i in terms:
        term = i.split()
        dic[term[0]] = int(term[1])

    # 각 개인 정보 별 유효 기간 판단
    for i in range(len(privacies)):
        private = privacies[i].split()
        if calc_date(today, private[0], dic[private[1]]):
            answer.append(i + 1)

    return answer

# privacies를 하나씩 체크하면서 폐기 여부 체 -> 수가 크지 않아서 시간초과 뜨지 않을 것 같음
