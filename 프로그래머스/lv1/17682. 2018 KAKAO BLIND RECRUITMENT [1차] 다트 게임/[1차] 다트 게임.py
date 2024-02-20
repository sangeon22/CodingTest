def solution(dartResult):
    answer = [0, 0, 0]
    a = dartResult.replace("S", "S,").replace("D", "D,").replace("T", "T,")
    arr = a.split(',')
    for i in range(len(arr)):
        if arr[i] != "":
            if arr[i][0] == "*":
                arr[i - 1] += "!"
                arr[i] = arr[i].replace("*", "")
            elif arr[i][0] == "#":
                arr[i - 1] += "#"
                arr[i] = arr[i].replace("#", "")

    for i in range(len(arr) - 1):
        arr[i] = arr[i].replace("S", "").replace("D", "**2").replace("T", "**3")

    idx = 0
    for i in arr:
        if idx == 3:
            break
        temp = 0
        if "#" not in i and '!' not in i:
            temp = eval(i)
        elif "#" in i:
            temp = 0 - eval(i.replace("#", ""))
        elif "!" in i:
            temp = eval(i.replace("!", "")) * 2
            if idx != 0:
                answer[idx - 1] *= 2
        answer[idx] = temp
        idx += 1

    return sum(answer)

