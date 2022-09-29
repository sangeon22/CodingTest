def solution(s):
    answer = ''
    
    answer += s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == " " and s[i] != " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    

#     for i in s.split(" "):
#         answer += i[0].upper()
#         answer += i[1:].lower()
#         answer+=" "
        
#     answer = answer[:-1]
    
#     count = 0
    
#     for i in range(len(s)):
#         if s[i] == " ":
#             answer+= " "
#             if s[i+1] != " ":
#                 count += 1
        
#         if s[i].isalpha():
#             if count == 1:
#                 answer += s[i].upper()
#             else:
#                 answer += s[i].lower()
#                 count += 1 
#         elif s[i].isdigit():
#             answer += s[i]
#             count += 1
    
    
    # for i in s:
    #     if i.alpha():
    #         if i.
    #     else:
    #         answer += i
    return answer