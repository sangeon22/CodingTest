'''
다이나믹 프로그래밍(동적 계획법, dp): 메모리를 적절히 사용하여 수행 시간 효율성으로 비약적으로 향상 시키는 방법
- 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장 -> 다시 계산 X
- 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑다운, 바텀업)

문제가 다음 조건을 만족할 때 다이나믹 프로그래밍 사용가능
1. 최적 부분 구조
    큰 문제를 작은 문제로 나눌 수 있고 작은 문제의 답을 모아 큰 문제를 해결
2. 중복되는 부분 문제
    동일한 작은 문제를 반복적으로 해결
'''

'''
피보나치 수열
1, 1, 2, 3, 5, 8, 13, 21 ...
점화식 : an = an-1 + an-2
'''


def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))


# 단순 재귀로 피보나치 수열을 계산하면 지수 시간 복잡도를 가지게 되고 수가 커지면 기하급수적으로 커짐
# 중복 부분 문제가 많음(피보나치를 트리로 만들어보면 예로 f(2)가 엄청 많음) => 중복 부분 문제를 미리 메모리에 기록
# 피보나치 수열은 위의 다이나믹 프로그래밍 조건 2가지를 만족
# 하향식(탑다운)에서 사용되는 메모이제이션(한 번 계산한 결과를 메모리 공간에 메모) 캐싱이라고도 함


# 탑다운 방식 dp => 재귀
def fibo_dp_top_down(x):
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산하지 않은 문제라면
    d[x] = fibo_dp_top_down(x - 1) + fibo_dp_top_down(x - 2)
    return d[x]


# 메모이제이션
d = [0] * 100
print(fibo_dp_top_down(99))



# 바텀업 방식 dp => 반복문
d1 = [0] * 100
d1[1] = 1
d1[2] = 1
n = 99

for i in range(3, n + 1):
    d1[i] = d1[i - 1] + d1[i - 2]
print(d1[n])


'''
다이나믹 프로그래밍과 분할 정복(퀵 정렬) 모두 최적 부분 구조를 가질 때 사용
1. 최적 부분 구조
    큰 문제를 작은 문제로 나눌 수 있고 작은 문제의 답을 모아 큰 문제를 해결
    
그러나 dp와 분할정복 차이점은
2. 중복되는 부분 문제
    동일한 작은 문제를 반복적으로 해결

퀵정렬에서 피벗을 통해 분할이 이뤄지고 피벗을 다시 처리하는 문제는 호출되지 않음
문제를 보고 어떤 알고리즘을 사용할 수 있는지 파악하는 것이 중요!!
완전탐색 -> 재귀 -> 코드 개선 겸 탑다운 방식 db 적용
'''