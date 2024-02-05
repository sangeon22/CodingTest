t = int(input())
for _ in range(t):
    change = int(input())
    a = change // 25
    change %= 25

    b = change // 10
    change %= 10

    c = change // 5
    change %= 5

    d = change // 1
    change %= 1

    print(f'{a} {b} {c} {d}')
