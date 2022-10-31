def solution(emergency):
    return [ sorted(emergency, reverse=True).index(i)+1 for i in emergency ]