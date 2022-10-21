def solution(before, after):
    if sorted(before) != sorted(after):
        return 0
    else:
        return 1