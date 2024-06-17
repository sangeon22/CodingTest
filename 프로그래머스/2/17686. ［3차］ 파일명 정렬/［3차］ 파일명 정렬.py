def solution(files):
    arr = []

    # 숫자를 기준으로 HEAD, NUMBER, TAIL로 분리
    for i in files:
        temp = []
        flag = 0

        # flag == 0
        head = ""

        # flag == 1
        number = ""

        # flag == 2
        tail = ""
        for j in i:
            # flag 값에 따라 head, number, tail 분류
            if flag == 1 and not j.isdigit():
                flag = 2
            elif flag != 2 and j.isdigit():
                flag = 1

            if flag == 0:
                head += j
            elif flag == 1:
                number += j
            elif flag == 2:
                tail += j

        temp.append(head)
        temp.append(number)
        temp.append(tail)
        arr.append(temp)

    # 정렬 함수
    sorted_arr = sorted(arr, key=lambda x: (x[0].lower(), int(x[1])))

    # 정렬된 결과를 파일 이름으로 재구성
    answer = ["".join(x) for x in sorted_arr]

    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# 기댓값 >	["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# ['img1.png', 'IMG01.GIF', 'img02.png', 'img2.JPG', 'img10.png', 'img12.png']
# 실행값 > ['IMG01.GIF', 'img1.png', 'img2.JPG', 'img02.png', 'img10.png', 'img12.png']
print(solution(files))
