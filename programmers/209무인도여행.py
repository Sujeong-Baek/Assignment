# https://school.programmers.co.kr/learn/courses/30/lessons/154540
from collections import deque
def solution(maps):
    answer = []
    visited= [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col].isdigit() and not visited[row][col]:
                answer.append(bfs(row, col, visited, maps))
    if not answer:
        return [-1]
    return sorted(answer)

def bfs(row, col, visited, maps):    
    queue=deque([(row,col)])
    stay=int(maps[row][col])
    visited[row][col]=True
    
    while queue:
        row, col =queue.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = row+dr , col+dc
            if 0<=nr<len(maps) and 0<=nc<len(maps[0]) and maps[nr][nc].isdigit() and not visited[nr][nc]:
                stay+=int(maps[nr][nc])
                visited[nr][nc]=True
                queue.append((nr,nc))
    return stay