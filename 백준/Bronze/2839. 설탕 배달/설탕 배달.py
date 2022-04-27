# 설탕봉지 최대한 적게
# N을 가져가야할 때, 5Kg과 3Kg봉지사용
# 5Kg로 나눈 후, 나머지를 3Kg로 사용하면?
# ex) 6의 경우, 3kgx2가 가능하지만 계산식대로면 5Kg+1Kg가 되버린다.
# => 3으로 나눠지면 3으로 나눠버린다.
# ex) 18kg의 경우, 5Kgx3 + 3Kg = 4봉지여야하지만, 3Kgx6 6봉지가 되어버린다.
# => 해결하는법..?
from itertools import count

N = int(input())
count = 0

while True:
    if N % 5 == 0:
        print(N//5 + count)
        break
    N -= 3
    count += 1

    if N<0:
        print(-1)
        break

