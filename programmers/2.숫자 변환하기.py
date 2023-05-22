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
        for sign, num in [("+", n), ("*", 2), ("*", 3)]:
            if sign == "+":
                nx=x+num
            elif sign == "*":
                nx=x*num
            if nx > y :
                continue
            if nx in visited:
                continue
            visited.add(nx)
            q.append((nx,time+1))
    return -1
