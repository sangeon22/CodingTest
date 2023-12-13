# 빅오 표기법
# 0(1) 상수시간
# O(logN) 로그시간
# O(N) 선형시간
# O(NlogN) 로그 선형 시간
# O(n**2)이차 시간
# O(n**3)삼차 시간
# O(2**n)지수 시간

# 시간 복잡도 계산 1 - N 개의 데이터의 합
arr = [3, 5, 1, 2, 4]
total = 0

for i in arr:
    total += i

print(total)
# 수행 시간은 데이터 개수 N에 비례 -> O(N) 선형 시간