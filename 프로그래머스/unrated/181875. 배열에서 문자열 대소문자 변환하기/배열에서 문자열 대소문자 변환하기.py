def solution(strArr):
    # return [strArr[i].upper() if i % 2 != 0 else strArr[i].lower() for i in range(len(strArr))]
    return [s.upper() if i % 2 != 0 else s.lower() for i, s in enumerate(strArr)]