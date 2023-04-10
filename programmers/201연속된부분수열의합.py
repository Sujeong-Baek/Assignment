# https://school.programmers.co.kr/learn/courses/30/lessons/178870
def solution(sequence, k):
    #연속된 el들의 합이 k가 되는 경우들 중
    #길이가 짧은 것
    #길이가 같은 경우 앞쪽에 나온 것
    #첫 인덱스와 마지막 인덱스 반환
    
    answer=[]
    cum_sum=[0]*(len(sequence)+1)
    min_len=float('inf')
    left=0
    right=1
    for i in range(1,len(cum_sum)):
        cum_sum[i]=cum_sum[i-1]+sequence[i-1]
    while right<len(cum_sum):
        if cum_sum[right]-cum_sum[left]==k:
            if right-left<min_len:
                answer=[left,right-1]
                min_len= right-left
            left+=1
        elif cum_sum[right]-cum_sum[left]<k:
            right+=1
        else:
            left+=1
    return answer