def solution(cards1, cards2, goal):
    idx1 = -1
    idx2 = -1
    
    for i in goal:
        if i in cards1:
            if idx1 == cards1.index(i) - 1:
                idx1 = cards1.index(i)
                continue
        elif i in cards2:
            if idx2 == cards2.index(i) - 1:
                idx2 = cards2.index(i)
                continue
        return "No"          
    return "Yes"