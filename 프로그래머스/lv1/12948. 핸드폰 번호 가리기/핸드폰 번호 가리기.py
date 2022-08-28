def solution(phone_number):
    answer = ''
    a = len(phone_number) -4
    answer += "*" * a
    answer += phone_number[-4:]
    
    return answer