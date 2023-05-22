# https://school.programmers.co.kr/learn/courses/30/lessons/169199
from collections import deque
ROBOT="R"
GOAL="G"
OBSTACLE = "D"

def find_index(board):
    for i, row in enumerate(board):
        for j, el in enumerate(row):
            if  el == ROBOT:
                return i, j
    

def bfs(board, rr, rc):
    R = len(board)
    C = len(board[0])
    visited = {(rr, rc)}
    queue = deque([(rr, rc, 0)])

    while queue:
        r, c, time =  queue.popleft()
        if board[r][c]==GOAL:
            return time
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr= r
            nc= c
            while 0 <= nr + dr < R and 0 <= nc + dc < C and board[nr + dr][nc + dc] != OBSTACLE:
                nr+=dr
                nc+=dc
            if (nr,nc) not in visited:
                visited.add((nr,nc))
                queue.append((nr,nc,time+1))
            # -1 = nr or nr == R or nc == -1 or nc == C or board[nr][nc] == OBSTACLE:            
    return -1


def solution(board):
    rr, rc = find_index(board)
    return bfs(board, rr, rc)

# "R" 위치에서 아래, 왼쪽, 위, 왼쪽, 아래, 오른쪽, 위 순서로 움직이면 7번 만에 "G"
# [
# "...D..R",
# ".D.G...",
# "....D.D",
# "D....D.",
# "..D...."