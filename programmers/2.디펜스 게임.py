# https://school.programmers.co.kr/learn/courses/30/lessons/142085
from heapq import heapify, heappop, heappush
def solution(n, k, enemy):
    answer = min(k, len(enemy))
    hq = enemy[:k]
    heapify(hq)
    for e in enemy[k:]:
        min_e=heappop(hq)
        n-=min(min_e, e)       
        if n < 0:
            break
        heappush(hq, max(min_e, e))    
        answer+=1
    return answer

lst = [1,2,3,4]

# lst[100]
# lst[:100]