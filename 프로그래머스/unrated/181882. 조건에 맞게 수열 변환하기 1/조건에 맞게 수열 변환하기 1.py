def solution(arr):
    # answer = []
    # for i in arr:
    #     if i >= 50 and i % 2 == 0:
    #         answer.append(i / 2)
    #     elif i < 50 and i % 2 != 0:
    #         answer.append(i * 2)
    #     else:
    #         answer.append(i)
    # return answer
    return [i / 2 if i >= 50 and i % 2 == 0 else (i * 2 if i < 50 and i % 2 != 0 else i)for i in arr]