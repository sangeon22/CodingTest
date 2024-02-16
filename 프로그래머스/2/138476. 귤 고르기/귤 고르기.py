from itertools import combinations
from collections import Counter

def solution(k, tangerine):
    # 시간 초과
    # comb = set(list(combinations(tangerine, k)))
    # return min([len(set(i)) for i in comb])
    answer = 0
    count = Counter(tangerine)
    total = 0
    for i in count.most_common():
        if total < k:
            total += i[1]
            answer += 1

    return answer