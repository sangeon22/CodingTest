from itertools import combinations


def solution(dots):
    incline = []
    for i in list(combinations(dots, 2)):
        incline.append((i[0][1] - i[1][1]) / (i[0][0] - i[1][0]))

    if len(incline) != len(set(incline)):
        return 1
    else:
        return 0