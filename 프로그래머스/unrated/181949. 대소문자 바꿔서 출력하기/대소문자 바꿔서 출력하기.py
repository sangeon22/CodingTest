str = input()
for i in str:
    if i.isupper():
        print(i.lower(), end="")
        continue
    print(i.upper(), end="")
            