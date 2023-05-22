# https://school.programmers.co.kr/learn/courses/30/lessons/159993
from collections import deque
START='S'
LEVER='L'
EXIT='E'
WALL='X'

def find_index(maps):
    for i, row in enumerate(maps):
        for j, el in enumerate(row):
            if el == START:
                sr, sc = i, j
            elif el == LEVER:
                lr, lc = i, j
            elif el == EXIT:
                er, ec = i, j
    return sr, sc, lr, lc, er, ec

def bfs(maps, sr, sc, er, ec):
    R, C = len(maps),len(maps[0])
    q = deque([(sr, sc, 0)])
    visited = set()
    visited.add((sr, sc))
    time = 0

    while q:
        r, c, time = q.popleft()
        
        if r == er and c == ec:
            return time
    
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if (nr, nc) in visited or maps[nr][nc] == WALL:
                continue
            
            visited.add((nr,nc))
            q.append((nr, nc, time + 1))
    return -1


def solution(maps):
    sx, sy, lx, ly, ex, ey = find_index(maps)
 
    lever_time = bfs(maps, sx, sy, lx, ly)
    exit_time = bfs(maps, lx, ly, ex, ey)

    return lever_time + exit_time if lever_time != -1 and exit_time != -1 else -1

# [0][0], [0][1]

# [x][y], [x][y+1]