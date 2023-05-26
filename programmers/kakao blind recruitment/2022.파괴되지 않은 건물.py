# https://school.programmers.co.kr/learn/courses/30/lessons/92344
def solution(board, skill):
    answer = 0
    for s in skill:
        tp, r1, c1, r2, c2, degree= s
        
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if tp==1:
                    board[r][c]-=degree
                else:
                    board[r][c]+=degree
                    
    answer = sum( [c > 0 for r in board for c in r ])
    return answer