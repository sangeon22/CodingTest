def solution(a, d, included):
    return sum([a + i*d for i in range(len(included)) if included[i]])
