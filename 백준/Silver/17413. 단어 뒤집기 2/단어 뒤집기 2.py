from sys import stdin

s = stdin.readline().rstrip()
stack = []
result = []
tag = False

for i in s:
    if i == '<':
        tag = True
        while stack:
            result.append(stack.pop())
    elif i == '>':
        tag = False
        result.append(i)
        continue

    if tag:
        result.append(i)
        continue
    elif not tag:
        if i == ' ':
            while stack:
                result.append(stack.pop())
            result.append(i)
        else:
            stack.append(i)

while stack:
    result.append(stack.pop())

print("".join(result))
# print("".join(word))
