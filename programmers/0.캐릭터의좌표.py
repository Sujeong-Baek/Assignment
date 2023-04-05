# https://school.programmers.co.kr/learn/courses/30/lessons/120861
def solution(keyinput, board):
    km={"up":[0,1], "down":[0,-1], "left":[-1,0], "right":[1,0]}
    r,c=0,0

    for key in keyinput:
        dr, dc = km[key][0],km[key][-1]
        nr,nc = r,c 
        if abs(nr+dr)<=board[0]//2 and abs(nc+dc)<=board[1]//2:
            nr+=dr
            nc+=dc
        else:
            nr,nc=r,c
        r,c=nr,nc        
    return [r,c]