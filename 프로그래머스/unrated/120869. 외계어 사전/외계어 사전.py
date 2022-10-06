def solution(spell, dic):
    li = []
    for i in dic:
        li.append("".join(sorted(i)))
    
    if "".join(sorted(spell)) in li:
        return 1
    else:
        return 2