def solution(a, b, n):
    answer = 0
    while True:
        if n // a == 0:
            break
            
        quo = n // a
        remain = n % a
        answer += quo * b
        n = (quo * b) + remain

    return answer