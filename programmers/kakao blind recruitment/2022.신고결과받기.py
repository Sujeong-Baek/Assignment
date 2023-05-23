# https://school.programmers.co.kr/learn/courses/30/lessons/92334
from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    reported2cnt=defaultdict(int)
    user2reported=defaultdict(set)
    
    for r in report:
        user, reported =r.split()
        if reported in user2reported[user]:
            continue
        user2reported[user].add(reported)
        reported2cnt[reported]+=1

    for user in id_list:
        mail_cnt=sum([reported2cnt[reported]>=k for reported in user2reported[user]])
        answer.append(mail_cnt)
            
    return answer