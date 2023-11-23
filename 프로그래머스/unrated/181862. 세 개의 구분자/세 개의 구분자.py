def solution(s):
    answer = []
    # temp = []
    # for i in s:
    #     if i not in ['a', 'b', 'c']:
    #         temp.append(i)
    #     else:
    #         answer.append(''.join(temp))
    #         temp.clear()
    #
    # answer.append(''.join(temp))
    # answer = list(filter(None, answer))
    # if len(answer) == 0:
    #     return ["EMPTY"]
    # return answer
    answer = list(filter(None, s.replace('a', ' ').replace('b', ' ').replace('c', ' ').split(' ')))
    return ['EMPTY'] if len(answer) == 0 else answer