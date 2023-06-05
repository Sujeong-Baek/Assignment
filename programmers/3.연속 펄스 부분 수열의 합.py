# https://school.programmers.co.kr/learn/courses/30/lessons/161988
def solution(sequence): 
    seq1=[] 
    seq2=[]

    for idx, s in enumerate(sequence):
        seq1.append(s*(-1)**idx)        
        seq2.append(s*(-1)**(idx+1))
    
    max_here1=max_whole1=0
    for s1 in seq1:        
        max_here1=max(s1, max_here1+s1)
        max_whole1=max(max_here1, max_whole1)
    
    max_here2=max_whole2=0
    for s2 in seq2:        
        max_here2=max(s2, max_here2+s2)
        max_whole2=max(max_here2, max_whole2)

    return max(max_whole1, max_whole2) 