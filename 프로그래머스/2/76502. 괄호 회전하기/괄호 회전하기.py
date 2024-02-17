from collections import deque


def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        stack = []

        for j in range(len("".join(s))):
            if s[j] in ["(", "{", "["]:
                stack.append(s[j])
            elif s[j] in ["}", ")", "]"]:
                if not stack:
                    break
                temp = stack.pop()
                if (temp == "{" and s[j] == "}") or (temp == "(" and s[j] == ")") or  (temp == "[" and s[j] == "]"):
                    if j == len("".join(s)) - 1 and not stack:
                        answer += 1
        s.rotate(-1)

    return answer
