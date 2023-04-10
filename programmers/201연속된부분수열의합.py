# https://school.programmers.co.kr/learn/courses/30/lessons/178870
def solution(sequence, k):
    #연속된 el들의 합이 k가 되는 경우들 중
    #길이가 짧은 것
    #길이가 같은 경우 앞쪽에 나온 것
    #첫 인덱스와 마지막 인덱스 반환
    len2index={}
    for i in range(len(sequence)):      
        sum_s=0
        end=0+i
        while sum_s<k and end<len(sequence):
            sum_s+=sequence[end]
            end+=1
        if sum_s==k:
            if end-1-i in len2index:
                continue
            len2index[end-1-i]=i,end-1
                
    return  len2index[min(len2index.keys())]