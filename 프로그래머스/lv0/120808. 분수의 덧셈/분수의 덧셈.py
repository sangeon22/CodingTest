import math


def solution(denum1, num1, denum2, num2):
    lcm = num1 * num2 // math.gcd(num1, num2)
    top = ((lcm // num1) * denum1) + ((lcm // num2) * denum2)

    return [top / math.gcd(top, lcm), lcm / math.gcd(top, lcm)]