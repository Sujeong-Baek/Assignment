# https://school.programmers.co.kr/learn/courses/30/lessons/120921
def solution(A, B):
    count=0
    while A != B :
        if count ==len(A)-1:
            return -1
        A=A[-1]+A[:-1]
        count+=1        
    return count