from collections import deque


def solution(cacheSize, cities):
    answer = 0

    # 캐시 사용하지 않는 경우, 모든 요소 cache miss 처리
    if cacheSize == 0:
        return len(cities) * 5
    deq = deque(maxlen=cacheSize)

    # 모든 요소 순차 처리
    for i in cities:
        i = i.lower()
        
        # 캐시 내 등록 되어 있는 요소의 경우, cache hit 처리
        if i in deq: # LRU 기법에 의해 가장 최근 참조 위치로 변경
            answer += 1
            deq.remove(i)
        else: # cache miss 처리
            answer += 5

        deq.append(i)
        
    return answer

# cache hit: 1s
# cache miss: 5s
# LRU
# deque 사용 ?
# 1. cacheSize 만큼 deque 크기 설정
# 2. deque에 해당 도시가 있으면 answer += 1 후 deque의 가장 최상단으로 해당 도시 이동
#                     없으면 answer += 5 후 deque의 가장 최상단에 해당 도시 추가