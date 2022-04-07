a, b = map(int, input().split())
if a == 0:
    a = a+24
    if a == 24 and b >= 45:
        a = 0

a = a * 60
total_hour = (a + b - 45) // 60
total_min = (a+b-45) % 60

print(total_hour,total_min, end =" ")
