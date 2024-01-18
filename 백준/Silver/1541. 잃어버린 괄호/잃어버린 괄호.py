s = input().split('-')
answer = sum(map(int, s[0].split('+')))

for i in s[1:]:
    answer -= sum(map(int, i.split('+')))

print(answer)