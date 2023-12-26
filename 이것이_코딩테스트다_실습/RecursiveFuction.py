'''
재귀함수: 자기 자신을 다시 호출하는 함수
- DFS를 구현할 때, 자주 사용하는 방식
- 종료조건을 반드시 명시(내부 스택구조로 파이썬 내부에서 RecursionError가 뜨긴함)
'''
def recursive_function(i):
    if i == 10:
        return
    print(f"{i}번째 재귀함수에서 {i + 1}번째 재귀함수 호출")
    recursive_function(i + 1)
    print(f"{i}번째 재귀함수 종료")


recursive_function(1)
# 1->2->3->....9 -> 이후 11번째 라인 출력(함수 종료)
print("==================================")


# 팩토리얼 기본 구현
def factorial_basic(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


# 팩토리얼 재귀함수 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # ...
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1
    # 점화식처럼


print(factorial_basic(5))
print(factorial_recursive(5))
print("==================================")

'''
최대공약수 계산(유클리드 호제법)
- 2개의 자연수에 대한 최대공약수 대표 구현 알고리즘
- 두 자연수(A> B)에서 A % B 값 => R(나머지)
- 이때, A와 B의 최대 공약수는 B와 R의 최대공약수와 같음
- ex) GCD(192, 162)
- 192/162
- 162/30
- 30/12
- 12/6 => 12는 6의 배수이니 6이 최대공약수
'''
# 라이브러리 이용
import math

print(math.gcd(192, 162))


# 최대공약수(유클리드 호제법) 재귀함수 구현
def gcd_recursive(a, b):
    if a % b == 0:
        return b
    return gcd_recursive(b, a % b)


print(gcd_recursive(192, 162))
print("==================================")

'''
수학적으로 점화식처럼 풀어나갈 수 있게 해주는 재귀함수 
때론 직관적이고 짧게 간결하게 풀 수도 있으나 가독성 문제가 있을 수 있으니 신중
반복문 <=> 재귀함수 서로 호환가능 => 양측 고민해보면서 풀기
DFS에 유용하게 사용되는 재귀함수
'''