# https://school.programmers.co.kr/learn/courses/30/lessons/150370#
from collections import defaultdict

def solution(today, terms, privacies):
    answer = [] 
    ty,tm,td=today.split('.')
    today=int(ty)*10000+int(tm)*100+int(td)
    
    typ2month = defaultdict(int)
    for term in terms:
        t,month=term.split()
        typ2month[t]=int(month)
        
    for i, privacy in enumerate(privacies,1):
        month=typ2month[privacy[-1]]
        if today >= calculator_date(month, privacy): 
            answer.append(i)        
    return answer

#약관 끝난 다음날 구하기
def calculator_date(month, privacy):
    py,pm,pd=map(int, privacy[:-1].split("."))
    py+=(pm+month-1)//12      
    return py*10000+ ((pm+month-1)%12+1)*100+pd