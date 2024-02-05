from itertools import product


def max_number(n):
    for i in range(len(n), 0, -1):
        product_list = [int("".join(i)) for i in product(x, repeat=i)]
        arr = [i for i in product_list if i <= int(n)]
        if arr:
            return max(arr)


x = ['4', '7']
print(max_number(input()))
