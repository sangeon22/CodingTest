def solution(numbers, hand):
    answer = ''
    key = {
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7:[2,0], 8:[2,1], 9:[2,2],
        '*':[3,0], 0:[3,1], '#':[3,2],
    }
    left = key['*']
    right = key['#']
    
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = key[i]
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = key[i]
        else:
            target = key[i]
            left_d = abs(target[0] - left[0]) + abs(target[1] - left[1])
            right_d = abs(target[0] - right[0]) + abs(target[1] - right[1])
            if left_d > right_d:
                answer += 'L'
                left = key[i]
            elif left_d < right_d:
                answer += 'R'
                right = key[i]
            else:
                if hand == "left":
                    answer += 'L'
                    left = key[i]
                else:
                    answer += 'R'
                    right = key[i]   
    
    return answer