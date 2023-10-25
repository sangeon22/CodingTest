def solution(my_string, target):
    try:
        my_string.index(target)
    except:
        return 0
    return 1