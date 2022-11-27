def solution(polynomial):
    li = polynomial.replace(" ", "").split('+')
    x_li = 0
    con_li = 0

    for i in li:
        if 'x' in i:
            if i == 'x':
                x_li += 1
            else:
                x_li += int(i.rstrip('x'))
        else:
            con_li += int(i)

    if x_li == 1:
        x_li = ""

    if x_li == 0:
        answer = "{}".format(con_li)
    elif con_li == 0:
        answer = "{}x".format(x_li)
    else:
        answer = "{}x + {}".format(x_li, con_li)

    return answer