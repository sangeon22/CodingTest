def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
        else:
            if (65 <= ord(i) <= 90 and 65 <= ord(i)+n <= 90) or (97 <= ord(i) <= 122 and 97 <= ord(i)+n <= 122):
                answer += chr(ord(i)+n)
            else:
                answer += chr(ord(i) -26 +n)
    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("Z", 10))
print(solution("a B z", 4))
print(solution(" aBZ", 20))
print(solution("y X Z", 4))
print(solution(" . h z", 20))

