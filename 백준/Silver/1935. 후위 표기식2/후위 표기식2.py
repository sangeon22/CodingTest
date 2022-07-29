from sys import stdin
# 후위표기법 숫자를 만나면 스택에 넣고 연산자가 나오면 두수를 꺼내 계산후 다시 스택에 넣음

# 피연산자 수
n = int(stdin.readline())

# 후위 표기식
s = stdin.readline().rstrip()

# 피연산자 대응값
li = []

# 계산할 때 쓸 스택
stack = []

for i in range(n):
    li.append(int(stdin.readline().rstrip()))

for i in s:
    if i == '+' or i == '-' or i == '*' or i == '/':
        str2 = stack.pop()
        str1 = stack.pop()

        if i == "+":
            stack.append(str1 + str2)
        elif i == "-":
            stack.append(str1 - str2)
        elif i == "*":
            stack.append(str1 * str2)
        elif i == "/":
            stack.append(str1 / str2)
    else:
        stack.append(li[ord(i) - ord('A')])


print('%.2f' %stack[0])

