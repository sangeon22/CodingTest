def solution(numlist, n):
    abs_li = []
    for i in numlist:
        abs_li.append(abs(i - n))

    return list(dict(sorted(list(zip(numlist, abs_li)), key=lambda x: (x[1], -x[0]))).keys())