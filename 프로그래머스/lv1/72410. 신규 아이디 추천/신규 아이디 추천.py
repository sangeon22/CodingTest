def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    for i in new_id:
        if i.isalpha() or i.isdigit() or i in "-_.":
            answer += i
    
    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer.strip('.')

    if answer == "":
        answer = "a"

    answer = answer[:15].rstrip('.')

    if len(answer) <= 2:
        while len(answer) <= 2:
            answer += answer[-1]
    
    return answer