def solution(arr):
    count = 0
    
    while True:
        temp = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                temp.append(i // 2)
            elif i < 50 and i % 2 == 1:
                temp.append(i * 2 +1)
            else:
                temp.append(i)
        count += 1
        if temp == arr:
            return count -1
        else:
            arr = temp