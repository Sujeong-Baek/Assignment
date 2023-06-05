# https://school.programmers.co.kr/learn/courses/30/lessons/161988
def solution(sequence):
    answer1, answer2 = 0, 0
    seq1=[]
    tmp1=[0]
    seq2=[]
    tmp2=[0]
    for idx, s in enumerate(sequence, 1):
        seq1.append(s*(-1)**idx)
        seq2.append(s*(-1)**(idx+1))
        
    for s in seq1:
        tmp1.append(tmp1[-1]+s)
        
    for s in seq2:
        tmp2.append(tmp1[-1]+s)

    for i in range(len(tmp1)):
        for j in range(i+1, len(tmp1)):
            answer1 = max(answer1, tmp1[j] - tmp1[i])
            
    for i in range(len(tmp2)):
        for j in range(i+1, len(tmp2)):
            answer2 = max(answer2, tmp2[j] - tmp2[i])
        
    return max(answer1, answer2)    