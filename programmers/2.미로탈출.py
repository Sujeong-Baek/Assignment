# https://school.programmers.co.kr/learn/courses/30/lessons/159993
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    sx, sy, ex, ey, lx, ly = -1, -1, -1, -1, -1, -1
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] 
    visited_l = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited_e = [[False] * len(maps[0]) for _ in range(len(maps))]
    

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'E':
                ex, ey = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j
    

    q = deque([(sx, sy, 0)])
    visited_l[sx][sy] = True
    lever_time = 0 
    while q:
        x, y, time = q.popleft()
        
        if x == lx and y == ly:
            lever_time = time
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited_l[nx][ny] or maps[nx][ny] == 'X':
                continue
            
            visited_l[nx][ny] = True
            q.append((nx, ny, time + 1))
                
    if not visited_l[lx][ly]:
        return -1
    

    q = deque([(lx, ly, lever_time)])
    visited_e[lx][ly] = True
    time = lever_time
    while q:
        x, y, time = q.popleft()
        
        if x == ex and y == ey:
            break
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited_e[nx][ny] or maps[nx][ny] == 'X':
                continue
            
            visited_e[nx][ny] = True
            q.append((nx, ny, time + 1))

    if not visited_e[ex][ey]:
        return -1
    
    return time
