def solution(numbers, k):
    answer = 0
    for i in range(len(numbers * k)):
        if i % 2 == 0:
            answer+=1
            if answer == k:
                return (numbers * k)[i]