while True:
    arr = list(map(int, input().split()))
    if arr[0] == -1:
        break
    
    answer = 0
    for i in arr:
        if i == 0:
            print(answer)
            break
        if i * 2 in arr:
            answer += 1
