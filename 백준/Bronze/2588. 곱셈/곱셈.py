a = int(input())
b = input()

r1 = a * int(b[2])
r2 = a * int(b[1])
r3 = a * int(b[0])

print(r1)
print(r2)
print(r3)
print(r1 + (r2 * 10) + (r3 * 100))
