def solution(wallpaper):
    lux = -1
    luy = 51
    ldx = -1
    ldy = -1
    count = len(wallpaper)

    for i in wallpaper:
        if '#' in i:
            if lux == -1:
                lux = i
            if i.index('#') < luy:
                luy = i.index('#')

    for i in wallpaper[::-1]:
        if '#' in i:
            if ldx == -1:
                ldx = count
            if i.rfind('#') > ldy:
                ldy = i.rfind('#')
        count -= 1

    return [wallpaper.index(lux), luy, ldx, ldy + 1]


# 1. 처음 나오는 #의 행        -> lux
# 2. 처음에 나오는 #의 열       -> luy
# 3. 마지막에 나오는 #의 행     -> rdx
# 4. 마지막에 나오는 #의 행     -> rdy
