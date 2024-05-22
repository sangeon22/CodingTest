import math


def solution(fees, records):
    answer = []

    # 1. 차량별 누적 시간 계산
    car_number_set = set()
    car_number_time_list = dict()

    # 차량 번호 추출
    for i in records:
        car_number_set.add(i.split()[1])

    car_number_list = sorted(car_number_set)
    # 차량 번호 별 시간 배열 초기화
    for i in car_number_list:
        car_number_time_list[i] = []

    # 차량 번호 별 시간 추출
    for i in records:
        time, car_number, breakdown = i.split()
        h, m = time.split(":")
        car_number_time_list[car_number].append(int(h) * 60 + int(m))

    for i in car_number_time_list.items():
        print(i[0])

        # 출차 기록이 없으면 23:59 출차 처리
        if len(i[1]) % 2 != 0:
            i[1].append(int(23) * 60 + int(59))

        # reverse 처리 후 계산
        time_list = i[1][::-1]
        differences = []

        # 2. 누적 시간별 요금 계산
        # 리스트에서 2개씩 차이를 계산
        for i in range(0, len(time_list), 2):
            difference = time_list[i] - time_list[i + 1]
            differences.append(difference)

        fee = sum(differences)
        if fee <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((fee - fees[0]) / fees[2]) * fees[3])

    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN",
           "06:00 0000 IN",
           "06:34 0000 OUT",
           "07:59 5961 OUT",
           "07:59 0148 IN",
           "18:59 0000 IN",
           "19:09 0148 OUT",
           "22:59 5961 IN",
           "23:00 5961 OUT"]
# 기댓값 	[14600, 34400, 5000]


print(solution(fees, records))
