a = int(input())
b = int(input())
c = int(input())
total = a * b * c
result = list(str(total))

for i in range(10):
    print(result.count(str(i)))