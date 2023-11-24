from collections import Counter


def solution(s):
    return sorted(Counter([len(i) for i in s]).most_common(), key=lambda x: x[1], reverse=True)[0][1]
