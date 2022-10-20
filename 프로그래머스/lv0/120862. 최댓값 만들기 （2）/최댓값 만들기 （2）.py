def solution(numbers):
    # return sorted(numbers)[-1] * sorted(numbers)[-2]

    # numbers.sort()
    # if numbers[0] * numbers[1] >= numbers[-1] * numbers[-2]:
    #     return numbers[0] * numbers[1]
    # else:
    #     return numbers[-1] * numbers[-2]

    return max(sorted(numbers)[-1] * sorted(numbers)[-2], sorted(numbers)[0] * sorted(numbers)[1])
