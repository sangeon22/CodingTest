while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif max(a, b) == b:
        print("No")
    else:
        print("Yes")

