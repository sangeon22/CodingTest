def solution(my_string):
    answer = []
    for i in my_string:
        if not i in answer:
            answer.append(i)
    return ''.join(answer)
    # return ''.join(dict.fromkeys(my_string))