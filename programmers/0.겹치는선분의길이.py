# https://school.programmers.co.kr/learn/courses/30/lessons/120876
def solution(lines):
    answer=0
    lines.sort()
    pivot_start=lines[0][0]
    pivot_end=lines[0][0]
    for start, end in lines:
        if max(pivot_start,start) < min(pivot_end,end): # 겹치는 경우
            answer+= min(pivot_end,end)-max(pivot_start,start)
            pivot_start=min(pivot_end,end)
            pivot_end=max(pivot_end,end)
        else:
            pivot_start=start
            pivot_end=end
    return answer

# 0         5 # end = 5
#    1           10 # end = 5,answer += 5 - 1
#      3        9   # end = 9, answer += 9 -5
end = 0

# 0         5 # pivot_start = -1, pivot_end = -1 >> pivot_start = -1, pivot_end = -1
#    1           10 # [1, 5] 4, s1, s2, e1, e2 >> [max(s1, s2), min(e1, e2)] >> start = min(e1, e2), end = max(e1, e2) , 5, 10
#      3        9   # 4, 