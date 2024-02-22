def solution(want, number, discount):
    answer = 0

    # 할인 품목에 희망 품목이 없으면 return 0
    for i in want:
        if i not in discount:
            return answer

    for i in range(len(discount)):
        # 해당 요일 할인 품목이 희망 품목에 없으면 해당 요일 pass
        if discount[i] not in want:
            continue
        
        # 희망 품목 개수 리스트
        count = number.copy()
        
        # 할인 품목 일자 기준으로 10일씩 슬라이싱 
        for j in discount[i:i + 10]:
            try:
                count[want.index(j)] -= 1
            except:
                # 희망 품목에 없는 경우, exception 방지
                break
            
            # 희망 품목을 충분히 샀는데 또 사면 해당 요일 PASS
            if -1 in count:
                break
                
            # 희망 품목 다 샀으면 해당 요일 만족이므로 answer ++    
            if sum(count) == 0:
                answer += 1

    return answer