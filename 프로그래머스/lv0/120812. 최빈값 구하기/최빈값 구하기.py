def solution(array):
    count_list = []
    idx = 0
    set_list = list(set(array))

    for i in set_list:
        count_list.append(array.count(i))

    for i in count_list:
        if i == max(count_list):
            break
        else:
            idx += 1
    a = set_list[idx]

    count_num = max(count_list)
    count_list.remove(count_num)

    if count_num in count_list:
        return -1
    else:
        return a