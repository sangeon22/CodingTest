a, b, c = map(int, input().split())

# (c*N) = a + (b*N)
# cN = a + bN
# cN-bN = a
# (c-b)N = a
# N = a/(c-b)

if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)