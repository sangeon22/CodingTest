from itertools import product

arr = [(i ** 2 + i) // 2 for i in range(1, 1001)]
for _ in range(int(input())):
    k = int(input())
    triangle_num = list(filter(lambda x: x < k, arr))
    if k in list(map(sum, product(triangle_num, repeat=3))):
        print(1)
        continue
    print(0)
