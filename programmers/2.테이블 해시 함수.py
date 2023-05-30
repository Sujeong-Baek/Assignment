# https://school.programmers.co.kr/learn/courses/30/lessons/147354
from collections import defaultdict
def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key = lambda x : (x[col-1], -x[0]))
    row2tuple = defaultdict(list)
    for row, d in enumerate(data,1):
        row2tuple[row] = d
        
    for row in range(row_begin, row_end+1):
        S_i = sum(i%row for i in row2tuple[row])
        answer ^= S_i 
    return answer