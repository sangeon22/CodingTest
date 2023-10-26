def solution(myString):
    return ''.join(['l' if ord(i) < ord('l') else i for i in myString])