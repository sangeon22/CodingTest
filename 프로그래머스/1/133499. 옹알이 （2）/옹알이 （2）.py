def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]

    # 첫번째 통과 코드
    # for i in babbling:
    #     string = ""
    #     pre_word = ""
    #     for j in range(len(i)):
    #         string += i[j]
    #         if len(string) == 0 and i[j] not in ["a", "y", "w", "m"]:
    #             break
    #
    #         if len(string) in [2, 3]:
    #             if string in word:
    #                 if pre_word == string:
    #                     break
    #                 pre_word = string
    #                 string = ""
    #                 if j == len(i) - 1:
    #                     answer += 1
    #                     break
    #         elif len(string) > 3:
    #             break

    # 두번째 통과 코드
    for i in babbling:
        if "ayaaya" in i or "yeye" in i or "woowoo" in i or "mama" in i:
            continue
        if not i.replace(word[0], " ").replace(word[1], " ").replace(word[2], " ").replace(word[3], " ").replace(" ", ""):
            answer += 1

    return answer
