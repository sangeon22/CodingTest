# 헷갈리는 부분, 모르는 부분만 기록

## 자료형
# 정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 사전


## 지수 표현 방식
# e나 E 다음에 오는 수는 10의 지수부
# return 실수형
# 1e9 => 10 ** 9
n = 1e9
print(n)

a = 10 ** 9
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


## 리스트 자료형
# 리스트 컴프리헨션
# 리스트 초기화 방식
# 2차원 리스트 n * n 초기화 방식
n = 5
m = 3
arr = [[0] * m for _ in range(n)]
arr[0][1] = 2
print(arr)

# 아래처럼 선언 시, 얕은 복사(주소값참조, 모두 같은 객체로 인식됨)
arr2 = [[0]*m] * n
arr2[0][1] = 3
print(arr2)

# 관련 메서드
arr3 = []
arr3.append("삽입할 값1") # O(1)
arr3.sort() # O(NlogN)
arr3.sort(reverse=True) # O(NlogN)
arr3.reverse() # O(N)
arr3.insert(1, "삽입할 값2") # O(N)
arr3.count("특정값") # O(N)
# arr3.remove("특정값") # O(N)


## 문자열 자료형
# 인덱싱, 슬라이싱 가능
a = "ABCDEF"
print(a[2:4])

# 특정 인덱스 값 변경 불가능(Immutable)
# a[0] = 'a'
# print(a)
# TypeError: 'str' object does not support item assignment


## 튜플 자료형
# () 소괄호 이용
# 리스트보다 공간 효율적(더 적은 메모리 사용)
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a)
print(a[1:4])

# 한 번 선언된 값 변경 불가능(Immutable)
# a[1] = 1
# print(a)
# TypeError: 'tuple' object does not support item assignment

# 리스트보다 튜플 사용하는 경우
# 1. 서로 다른 성질의 데이터를 묶어서 관리할 때
#    최단 경로 알고리즘 -> (비용, 노드번호)의 형태로 자주 사용
# 2. 데이터의 나열을 해싱의 키 값으로 사용해야 할 때
#    튜플은 리스트와 달리 Immutable하기에 키 값으로 사용 가능
# 3. 리스트보다 메모리 효율적으로 사용해야할 때


## 사전 자료형 dic
# 키-값(Key-Value) 쌍을 가지는 데이터
# 리스트, 튜플이 값을 순차적으로 저장하는 것과 대비됨 -> 인덱싱 불가
# Immutable 한 값을 키로 사용
# 사전 자료형은 내부적으로 해시테이블(HashTable) 이용 -> 조회, 수정의 시간 복잡도 -> O(1)

dic = dict()
dic['사과'] = 'Apple'
dic['바나나'] = 'Banana'
dic['코코넛'] = 'Coconut'
print(dic)

dic2 = {
    '홍길동': 97,
    '이순신': 98
}
print(dic2)

# 해당 키 존재하는지 확인
print('사과' in dic)
print('수박' in dic)

# 키 데이터만 뽑으려면
# dic 객체로 반환되니 list로 변환
print(list(dic.keys()))
for i in dic.keys():
    print(i)

# 값 데이터만 뽑으로면
print(list(dic.values()))
for i in dic.values():
    print(i)

# 각 키에 따른 값 데이터 출력
for key in dic.keys():
    print(dic[key])


## 집합 자료형 set
# 중복 허용X
# 순서 X
# 존재 유무 체크에 이용 용이
# 집합은 리스트 or 문자열로 초기화
# => set() 사용
# -> ({})안에 쉼표(,)를 기준으로 구분하여 삽입하여 초기화
# 사전 자료형 dic처럼 조회, 수정의 시간 복잡도 -> O(1)
a = set([1, 1, 2, 2, 3, 4, 5, 5])
print(a)

b = {1, 1, 2, 2, 3, 4, 5, 5}
print(b)

# 합집합, 차집합, 교집합 사용 가능
a = {1, 2, 3, 4, 5}
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)
# union도 결과는 같은데 뭐지 차집합, 교집합은 자동 완성에 안뜬다..
print(a.union(b))

# 차집합
print(a - b)
# 알아보니 차집합도 존재
print(a.difference(b))

# 교집합
print(a & b)
# 교집합도 존재
print(a.intersection(b))
# 2개 이상의 set에서는 .intersection_update 사용하는 듯함

# 원소 추가
c = {1, 2, 3}
c.add(4)
print(c)

# 원소 여러 개 추가 (아래 둘 다 되는 듯함)
c.update([5, 6])
c.update({7, 8})
print(c)

# 특정 원소 삭제
c.remove(3)
print(c)


## 기본 입출력
# map() => 리스트의 모든 원소에 특정한 함수 적용
# a = list(map(int, input().split()))
# b, c, d = map(int, input().split())
# print(b, c, d)

# 더 빠른 입출력
# 입력 후 개행(Enter)가 입력 => rstrip()
from sys import stdin
# a = stdin.readline().rstrip()
# print(a)

# f-string
print(f"테스트 {c}입니다.")

# format도 있었는데 뭔 차이지
# 직관적인건 f-string 인듯
# 찾아보니 %d, %s 방식 -> .format 방식(python3) -> f-string 방식(python 3.6) 순으로 등장
# + f-string은 산술연산 지원 {a+b}
# + 성능상으로도 유리 => 상수 및 함수를 사용하는 게 아니라서 런타임 단계에서 사용되니 성능상 유리하다고 한다.
# + 변수명이 길면 단점이 되기도 함
print("테스트 {}, {} 입니다".format(c, a))
print("테스트 {1}, {0} 입니다".format(c, a))


## 조건문, 반복문
# x in 리스트, 튜플, 문자열, 딕셔너리 모두 사용 가능


## 함수, 람다식
# 내장 함수 => input, print, split 등
# 사용자 정의 함수
def func(param):
    return param + 1

print(func(1))

# 전역 변수
# 함수 바깥의 변수를 사용하고자 한다면 global 사용
a = 10
def func():
    # a += 1
    # UnboundLocalError: local variable 'a' referenced before assignment
    # 그러나 참조만 한다면 에러 X
    # 전역변수 리스트는 global X
    global a
    a += 1
    print(a)

func()

# 함수 패킹 여러 개 반환 값
def operator(a, b):
    plus = a + b
    minus = a - b
    multiplication = a * b
    division = a / b
    return plus, minus, multiplication, division

a, b, c, d = operator(10, 3)
print(a, b, c, d)

# 람다(익명함수)
print((lambda a, b: a + b)(1,2))

# 키 값 정렬
arr = [('c', 99), ('a', 97), ('b', 98), ('A', 65)]
print(sorted(arr, key=lambda x:x[1]))

# 2개 리스트 각 인덱스 합
li1 = [1, 2, 3, 4, 5]
li2 = [6, 7, 8, 9, 10]
print(list(map(lambda x, y: x + y, li1, li2)))
