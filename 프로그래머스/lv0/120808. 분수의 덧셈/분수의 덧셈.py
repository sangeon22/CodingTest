import math


def solution(denum1, num1, denum2, num2):
    # 첫번째 풀이
    # lcm = num1 * num2 // math.gcd(num1, num2)
    # top = ((lcm // num1) * denum1) + ((lcm // num2) * denum2)
    #
    # return [top / math.gcd(top, lcm), lcm / math.gcd(top, lcm)]

    # 두번째 풀이
    # 2개 분수 합치기
    denum = (denum1 * num2) + (denum2 * num1)
    num = (num1 * num2)

    # 최대공약수로 약분 -> 기약분수
    return [denum // math.gcd(denum, num), num // math.gcd(denum, num)]
