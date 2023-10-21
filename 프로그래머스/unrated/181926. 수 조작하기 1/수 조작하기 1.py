def solution(n, control):
    return n + eval(control.replace('w',"+1").replace('s',"-1").replace('d',"+10").replace('a',"-10"))