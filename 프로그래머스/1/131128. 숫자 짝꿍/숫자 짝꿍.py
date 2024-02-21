from collections import Counter


def solution(X, Y):
    arr = []
    count_x = Counter(X)
    count_y = Counter(Y)
    intersection_num = set(count_x.keys()).intersection(set(count_y.keys()))

    for i in intersection_num:
        print(f"[count_x] key:{i}, value:{count_x.get(i)}")
        print(f"[count_y] key:{i}, value:{count_y.get(i)}")
        cnt = min(int(count_x.get(i)), int(count_y.get(i)))
        for _ in range(cnt):
            arr.append(i)
    arr.sort(reverse=True)
    if not arr:
        return str(-1)
    elif "".join(arr).replace("0", "") == "":
        return str(0)
    return "".join(arr)