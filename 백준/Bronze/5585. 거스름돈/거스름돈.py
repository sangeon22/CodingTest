change = 1000 - int(input())
answer = 0
while change != 0:
    money = 0
    if change >= 500:
        money = 500
    elif change >= 100:
        money = 100
    elif change >= 50:
        money = 50
    elif change >= 10:
        money = 10
    elif change >= 5:
        money = 5
    elif change >= 1:
        money = 1

    if money != 0:
        answer += (change // money)
        change %= money
print(answer)
