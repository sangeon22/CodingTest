def solution(my_string):
    li = list(my_string)
    
    if 'a' in li:
        while 'a' in li: 
            li.remove('a')
    
    if 'e' in li:
        while 'e' in li: 
            li.remove('e')
        
    if 'i' in li:
        while 'i' in li: 
            li.remove('i')
        
    if 'o' in li:
        while 'o' in li: 
            li.remove('o')
        
    if 'u' in li:
        while 'u' in li: 
            li.remove('u')
    
    return "".join(li)
        