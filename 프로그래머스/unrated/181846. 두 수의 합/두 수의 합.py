def solution(a, b):
    s = a + "+" + b
    if s != "0":
        return str(eval(s))
    return "0"