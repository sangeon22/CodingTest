t = int(input())

for i in range(t):
    n = int(input())
    max = 0
    max_sch = ""
    for j in range(n):
        s, l = input().split()
        l = int(l)
        if l > max:
            max = l
            max_sch = s
    print(max_sch)
