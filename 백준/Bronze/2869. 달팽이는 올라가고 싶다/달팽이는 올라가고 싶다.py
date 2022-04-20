#         continue
#     else:
#         break
# print(day)

# day 1 낮에 2 밤에 -1 총 1
# day 2 낮에 2 밤에 -1 총 2
# day 3 낮에 2 밤에 -1 총 3
# day 4 낮에 2 밤에 -1 총 5 -1

# v = (a-b)day + a
# v-a = (a-b)day
# (v-a)/(a-b) = day

import math
a, b, v = map(int, input().split())
day = math.ceil((v-a)/(a-b)) + 1
print(day)