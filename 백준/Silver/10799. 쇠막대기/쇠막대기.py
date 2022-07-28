from sys import stdin

a = stdin.readline().rstrip()

stack = []
sum = 0

# 중요 !! '(' 갯수는 막대기의 갯수를 의미
# '(' 바로다음 ')'이면 레이저니까 막대기 갯수에 관여 x?


for i in range(len(a)):
    # '(' 들어왔을 때
    if a[i] == '(':
        stack.append('(')

    # ')' 들어왔을 때
    else:
        #바로 전이 '(' 이면 레이저
        if a[i-1] == '(':
            stack.pop()
            sum += len(stack)

        #바로 전이 ')'이면 쇠막대기
        else:
            stack.pop()
            sum += 1

print(sum)