# https://school.programmers.co.kr/learn/courses/30/lessons/120866
def solution(board):
    answer = 0
    boom_list=[]
    drdc=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    #폭탄을 찾고    
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c]==1:            
                boom_list.append((r,c))
    #주변 0을 1로 바꾸기        
    for r,c in boom_list:
        for dr,dc in drdc:            
            nr,nc=r+dr,c+dc
            if 0<=nr<len(board) and 0<=nc<len(board):
                board[nr][nc]=1
    
    #0만 카운트
    for b in board:
        answer+=b.count(0)
    return answer