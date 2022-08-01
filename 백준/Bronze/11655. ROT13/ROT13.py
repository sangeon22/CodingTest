from sys import stdin

word = stdin.readline().rstrip("\n")
result = ''
for i in word:

    if i.isupper():
        i = ord(i) + 13
        if i > 90:
            i -= 26
        result += chr(i)

    elif i.islower():
        i = ord(i) + 13
        if i > 122:
            i -= 26
        result += chr(i)

    else:
        result += i

print(result)
