# https://school.programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reported2user={}
    mail_id=[]
    
    for r in report:
        user, reported =r.split()
        if reported in reported2user:
            reported2user[reported].add(user)                  
        else:
            reported2user[reported]=set()
            reported2user[reported].add(user)

    for ide in id_list:
        if ide in reported2user and len(reported2user[ide])>=k:
            mail_id.extend(list(reported2user[ide]))

    for idx, ide in enumerate(id_list):     
        answer[idx]= mail_id.count(ide)
            
    return answer