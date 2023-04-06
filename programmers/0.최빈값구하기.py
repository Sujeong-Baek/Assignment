# https://school.programmers.co.kr/learn/courses/30/lessons/120812
from collections import defaultdict

def solution(array):
    el2count = defaultdict(int)
    answer=[]
    for el in array:        
        el2count[el]+=1
    
    max_count=max(el2count.values())
 
    for el in el2count:
        if el2count[el]==max_count:
            answer.append(el)

    return -1 if len(answer)>1 else answer[0]