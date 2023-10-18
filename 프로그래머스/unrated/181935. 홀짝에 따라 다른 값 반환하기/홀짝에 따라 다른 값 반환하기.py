def solution(n):
    odd = []
    even = []
    flag = "odd"
    
    if n % 2 == 0:
        flag = "even"
        
    [even.append(i) if i % 2 == 0 else odd.append(i) for i in range(1, n +1)]
        
    return sum(odd) if flag == "odd" else sum([i**2 for i in even])
