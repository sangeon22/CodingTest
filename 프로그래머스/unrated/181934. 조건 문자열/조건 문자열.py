def solution(ineq, eq, n, m):
    if eq == "!":
        if ineq == ">":
            return int(bool(n>m))
        return int(bool(n<m))   
    else:
        if ineq == ">":
            return int(bool(n>=m))
        return int(bool(n<=m))   
        
    
   