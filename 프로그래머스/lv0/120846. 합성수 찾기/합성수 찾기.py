def prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count >= 3:
        return False
    else:
        return True


def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if not prime(i):
            answer += 1
    return answer