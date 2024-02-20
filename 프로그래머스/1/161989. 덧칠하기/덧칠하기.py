def solution(n, m, section):
    answer = 0
    i = 1
    while i <= n:
        if i in section:
            section.pop(section.index(i))
            answer += 1
            if len(section):
                if section[0] - i > m:
                    i = section[0]
                else:
                    i += m
        else:
            i += 1
    # roller = []
    # c_section = section.copy()
    #
    # for i in section:
    #     if i not in roller:
    #         temp = [j for j in range(i, i + m)]
    #         for k in temp:
    #             if k in c_section:
    #                 c_section.pop(c_section.index(k))
    #                 answer += 1
    #                 roller = temp
    #                 break

    return answer