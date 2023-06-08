# https://school.programmers.co.kr/learn/courses/30/lessons/152995
from collections import defaultdict

def solution(scores):
    min_s0=float('inf')
    min_s0_idxs=set()
    min_s1=float('inf')
    min_s1_idxs=set()
    idx2total=defaultdict(int) 

    for idx, (s0, s1) in enumerate(scores):
        if min_s0>s0:
            min_s0=s0
            min_s0_idxs={idx}
        elif min_s0==s0:
            min_s0_idxs.add(idx)
        if min_s1>s1:
            min_s1=s1
            min_s1_idxs={idx}
        elif min_s1==s1:
            min_s1_idxs.add(idx)
        idx2total[idx]=s0+s1

    no_incentive=min_s0_idxs.intersection(min_s1_idxs)
    
    if 0 in no_incentive:
        return -1
    else:
        for idx in no_incentive:
            idx2total.pop(idx)
        idx2total=dict(sorted(idx2total.items(), key=lambda x:x[1],reverse=True))
        
        rank=0
        prev_score = float('inf')
        for idx, total in enumerate(idx2total.values()):
            if total != prev_score:
                rank = idx + 1
            if idx2total[0] == total:
                return rank
            prev_score = total