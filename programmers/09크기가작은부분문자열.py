# https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    
    count=0
    len_t=len(t)
    len_p=len(p)
    
    for i in range(len_t-len_p+1):        
        if int(t[i:i+len_p]) <=int(p):
            count+=1
    return count