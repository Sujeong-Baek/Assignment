# https://school.programmers.co.kr/learn/courses/30/lessons/154538
from collections import deque

def solution(x, y, n):
    
    q=deque([(x, 0)])
    visited = set()
    visited.add(x)
    time = 0
   
    while q:
        num, time = q.popleft()
        if num == y:
            return time
        for sign, number in [("+", n), ("*", 2), ("*", 3)]:
            if sign == "+":
                num+=number
            elif sign == "*":
                num*=number
            if num > y :
                continue
            if num in visited :
                continue
            
            visited.add(num)
            q.append((num, time+1))    
    return -1

print(solution(10, 40, 5))