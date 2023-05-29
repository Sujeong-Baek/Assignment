# https://school.programmers.co.kr/learn/courses/30/lessons/154538
from collections import deque

def solution(x, y, n):
    
    q=deque([(x, 0)])
    visited=set([x])
    time = 0

    while q:
        x, time = q.popleft()
        if x == y:
            return time
        for num in [x + n, 2*x, 3*x]:
            if num in visited:
                continue
            visited.add(num)
            q.append((num,time+1))
    return -1
