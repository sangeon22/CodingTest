while True:
    a = list(map(int, input().split()))
    if sum(a) == 0:
        break

    a.sort(reverse=True)
    x = a[0]**2
    y = a[1]**2
    z = a[2]**2

    if y + z == x:
        print("right")
    else:
        print("wrong")
