# @ = x3
# % = +5
# # -7

T = int(input())

for i in range(T):
    a = input().split()
    temp = float(a[0])

    for j in range(len(a)):
        if a[j] == "@":
            temp = temp * 3
        elif a[j] == "%":
            temp = temp + 5
        elif a[j] == "#":
            temp = temp - 7
    print("%0.2f" %temp)
