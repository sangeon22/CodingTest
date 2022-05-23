v = int(input())
a = list(input())

if a.count('A') > a.count('B'):
    print("A")
elif a.count('A') < a.count('B'):
    print("B")
else:
    print("Tie")
