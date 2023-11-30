def solution(phone_book):
    dic = {}
    
    for i in phone_book:
        dic[i] = [j for j in i]
    
    for i in dic:
        temp = ""
        for j in i:
            try:
                if dic[temp] and dic[temp] != i:
                    return False
            except:
                pass
            temp += j
    return True