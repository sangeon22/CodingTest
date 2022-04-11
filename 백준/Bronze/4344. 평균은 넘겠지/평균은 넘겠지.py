c = int(input())
for _ in range(c):
    a = list(map(int, input().split()))
    count = 0
    for i in a[1:]:
        avg = sum(a[1:]) / a[0]
        if i > avg:
            count += 1

    total = count / a[0] * 100
    print('%.3f' %total + '%')
