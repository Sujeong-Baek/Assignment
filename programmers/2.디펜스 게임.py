# https://school.programmers.co.kr/learn/courses/30/lessons/142085
from heapq import heappop, heappush
def solution(n, k, enemy):
    answer = 0
    hq=[]
    for e in enemy:
        if k>0:
            heappush(hq, e)
            k-=1
        else:
            min_e=heappop(hq)
            if e<min_e and n-e>=0:
                heappush(hq, min_e)
                n-=e
            elif e>=min_e and n-min_e>=0:
                heappush(hq, e)
                n-=min_e                   
            else:
                break
        answer+=1
    return answer