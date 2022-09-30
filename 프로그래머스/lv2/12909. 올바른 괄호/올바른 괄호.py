def solution(s):
    answer = True
    stack = []

    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                answer = False
                break

    if len(stack) != 0:
        answer = False

    return answer