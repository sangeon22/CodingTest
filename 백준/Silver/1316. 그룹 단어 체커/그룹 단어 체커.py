n = int(input())
count = n
for i in range(n):
    word = input().lower()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1: ]:
            count -= 1
            break
print(count)