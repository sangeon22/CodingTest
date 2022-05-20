a = list()
sum = 0

for _ in range(5):
    a.append(int(input()))

for i in a:
    if i < 40:
        sum += 40
    else:
        sum += i

avg = sum / 5
print(int(avg))