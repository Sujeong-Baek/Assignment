# https://school.programmers.co.kr/learn/courses/30/lessons/159993
from collections import deque
def find_index(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j
            elif maps[i][j] == 'E':
                ex, ey = i, j
    return sx, sy, lx, ly, ex, ey

def bfs(maps, sx, sy, ex, ey):
    n, m = len(maps),len(maps[0])
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] 
    q = deque([(sx, sy, 0)])
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[sx][sy] = True
    time = 0

    while q:
        x, y, time = q.popleft()
        
        if x == ex and y == ey:
            return time
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] or maps[nx][ny] == 'X':
                continue
            
            visited[nx][ny] = True
            q.append((nx, ny, time + 1))
                
    if not visited[ex][ey]:
        return -1

def solution(maps):
    sx, sy, lx, ly, ex, ey = find_index(maps)
 
    lever_time = bfs(maps, sx, sy, lx, ly)
    exit_time = bfs(maps, lx, ly, ex, ey)

    return lever_time + exit_time if lever_time != -1 and exit_time != -1 else -1