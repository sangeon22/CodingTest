def solution(babbling):
    answer = 0
    for i in babbling:
        if "aya" or "ye" or "woo" or "ma" in i:
            temp = i.replace("aya", "*").replace("ye", "*").replace("woo", "*").replace("ma", "*")
            temp = temp.replace("*", "")
            if not temp:
                answer += 1

    return answer