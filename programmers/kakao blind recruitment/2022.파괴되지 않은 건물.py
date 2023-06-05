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

#누적합
lst = [1, 2, 3, 4, 5]
cumulative_sum = [0]
for i in lst:
    cumulative_sum.append(cumulative_sum[-1] + i)
cumulative_sum = cumulative_sum[1:]

def solution2(board, skill):
    answer=0
    tmp=[[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree=-degree
        tmp[r1][c1]+=degree
        tmp[r1][c2+1]-=degree
        tmp[r2+1][c1]-=degree
        tmp[r2+1][c2+1]+=degree
    #행
    for r in range(len(tmp)-1):
        for c in range(len(tmp[0])-1):
            tmp[r][c+1]+=tmp[r][c]
    #열
    for r in range(len(tmp)-1):
        for c in range(len(tmp[0])-1):
            tmp[r+1][c]+=tmp[r][c]
            
    #board와 합치기
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c]+=tmp[r][c]
            if board[r][c]>0:
                answer+=1
    return answer