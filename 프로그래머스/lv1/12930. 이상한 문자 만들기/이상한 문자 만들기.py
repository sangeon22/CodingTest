def solution(s):
    answer = ''
    count = 0
    for i in range(len(s)):
        if s[i] == " ":
            count = 0
            answer += " "
        else:
            if count % 2 == 0:
                count += 1
                answer += s[i].upper()
            else:
                count += 1
                answer += s[i].lower()

    return answer