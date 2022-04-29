M = int(input())
N = int(input())
a = []

if M > N:
    N = int(input())

for i in range(M, N + 1):
    for j in range(2, i+1):
        if j == i:
            a.append(i)
        if i % j == 0:
            break

if not a:
    print("-1")
else:
    print(sum(a))
    print(min(a))
