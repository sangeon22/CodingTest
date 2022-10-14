def solution(sides):
    sides.sort()
    print(sides)
    return 1 if sides[0]+sides[1] > sides[-1] else 2