def solution(age):
    # dic = { 0:'a', 1:'b', 2:'c', 3:'d', 4:'e',
    #         5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    
    answer = ""
    result = "abcdefghij"
    
    for i in str(age):
        answer += result[int(i)]
        
    return answer