def solution(numbers, target):
    leaves = [0]

    for i in numbers:
        temp = []
        for j in leaves:
            temp.append(j + i)
            temp.append(j - i)
            
        leaves = temp
        
    return leaves.count(target)