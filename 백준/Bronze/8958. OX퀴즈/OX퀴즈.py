n = int(input())
for _ in range(n):
    count = 0
    score = 0
    a = list(input())
    for i in range(len(a)):
        if a[i] == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)
