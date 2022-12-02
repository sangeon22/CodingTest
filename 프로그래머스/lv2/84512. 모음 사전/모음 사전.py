import itertools


def solution(word):
    # l1 = ['A', 'E', 'I', 'O', 'U']
    # li1 = list(itertools.product(l1, repeat=1))
    # li2 = list(itertools.product(l1, repeat=2))
    # li3 = list(itertools.product(l1, repeat=3))
    # li4 = list(itertools.product(l1, repeat=4))
    # li5 = list(itertools.product(l1, repeat=5))
    #
    # li = li1 + li2 + li3 + li4 + li5
    #
    # li.sort()
    # count = 0
    # for i in li:
    #     count += 1
    #     if "".join(i) == word:
    #         return count

    return sorted(["".join(j) for i in range(1,6) for j in itertools.product(['A','E','I','O','U'], repeat=i)]).index(word)+1