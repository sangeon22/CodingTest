# 자료형
# 정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 사전

# 지수 표현 방식
# e나 E 다음에 오는 수는 10의 지수부
# return 실수형
# 1e9 => 10 ** 9
n = 1e9
print(n)

a = 10**9
print(n)


# 실수값은 10진수 체계에서 정확하지 않다 ex) 10 / 3 = 0.33333....
# 이진수로 계산하는 컴퓨터는 더욱 미세한 오차 존재
# 아래처럼 0.89999이기 때문에 False가 나온다.
b = 0.3 + 0.6
print(b)
print(True) if b == 0.9 else print(False)

# 따라서 round() 함수 사용 권장
# round(실수, 반올림하여 나오는 소수점 자리)
print(round(b, 4))
print(True) if round(b, 4) else print(False)

