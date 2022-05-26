t = int(input())

if t % 10 != 0:
    print(-1)

else:
    a = t // 300
    b = (t % 300) // 60
    c = ((t % 300) % 60) // 10
    print(a, b, c)

# if t / a > 0:
#     a1 = t // a
#     b1 = (t % a) // b
#     c1 = ((t % a) % b) // c
#
# else:
#     a1 = 0
#     b1 = t // b
#     c1 = (t % b) // c
#
# if a1+b1+c1 == t:
#     print(a1, b1, c1)
# else:
#     print(-1)
