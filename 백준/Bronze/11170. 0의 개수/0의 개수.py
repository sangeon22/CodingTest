for _ in range(int(input())):
    n, m = map(int, input().split())
    print(''.join([str(i) for i in range(n, m + 1)]).count("0"))