def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        string = ""
        pre_word = ""
        for j in range(len(i)):
            string += i[j]
            if len(string) == 0 and i[j] not in ["a", "y", "w", "m"]:
                break

            if len(string) in [2, 3]:
                if string in word:
                    if pre_word == string:
                        break
                    pre_word = string
                    string = ""
                    if j == len(i) - 1:
                        answer += 1
                        break
            elif len(string) > 3:
                break
    return answer
