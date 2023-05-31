# https://school.programmers.co.kr/learn/courses/30/lessons/142085
from heapq import heappop, heappush
def solution(n, k, enemy):
    answer = 0
    hq=[]
    for e in enemy:
        if k>0:
            heappush(hq, e)
            k-=1
            answer+=1
        else:
            a=heappop(hq)
            if n-a >=0:
                n-=a
                heappush(hq,e)
                answer+=1
            else:
                break
    return answer