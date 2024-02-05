s = input()
w = input()
answer = 0

while True:
    if w in s:
        s = s.replace(w, '!', 1)
        answer += 1
    else:
        break
print(answer)