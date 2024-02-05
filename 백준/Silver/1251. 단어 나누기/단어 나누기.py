# 틀림
# s = input() + "!"
# temp = ""
# i, j = 0, 1
# answer = []
# while i != len(s) - 3:
#     j = i + 1
#     k = j
#     while s[j] != "!":
#         arr = [l for l in f"{temp}/{s[i]}/{s[i + 1:j]}/{s[j:-1]}".split('/') if l != '']
#         arr = ["".join(list(reversed(m))) for m in arr]
#         if len("".join(arr)) == len(s) - 1:
#             print("".join(arr))
#             answer.append("".join(arr))
#         j += 1
#     temp = s[:k]
#     i += 1
# print(sorted(answer)[0])

s = input()
result = "z" * len(s)
for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s)):
        result = min(result, s[:i][::-1] + s[i:j][::-1] + s[j:][::-1])
print(result)
