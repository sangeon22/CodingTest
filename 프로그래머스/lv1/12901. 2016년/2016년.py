        
def solution(a, b):
    answer = ''
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    mon = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = 0
    
    for i in range(1, a):
        days += mon[i-1]
    
    days += b
    answer = day[(days % 7) -1]
    
    return answer