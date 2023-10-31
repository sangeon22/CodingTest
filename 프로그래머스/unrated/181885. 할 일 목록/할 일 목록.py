def solution(todo_list, finished):
    # return [i for i in dict(zip(todo_list,finished)) if not dict(zip(todo_list,finished)).get(i) ]
    return [todo for idx, todo in enumerate(todo_list) if not finished[idx]]
