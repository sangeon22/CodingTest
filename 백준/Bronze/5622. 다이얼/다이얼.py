a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input().upper()
count = 0
# WA
for i in range(len(word)):
    for j in range(len(a)):
        if (word[i] in a[j]) == True:
            count += 3+j

print(count)