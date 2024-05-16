def solution(data, ext, val_ext, sort_by):
    answer = []
    idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    standard_than = idx[ext]
    standard_sort = idx[sort_by]
    for i in data:
        if i[standard_than] < val_ext:
            answer.append(i)

    answer.sort(key=lambda x: x[standard_sort])
    return answer


data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"
# result [[3,20300401,10,8],[1,20300104,100,80]]