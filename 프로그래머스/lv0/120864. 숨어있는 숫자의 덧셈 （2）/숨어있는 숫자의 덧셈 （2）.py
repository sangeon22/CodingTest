def solution(my_string):
    answer = 0
    temp = ""
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            if i+1 != len(my_string) and my_string[i + 1].isdigit():
                temp += my_string[i]
            else:
                temp += my_string[i]
                answer += int(temp)
                temp = ""

    return answer