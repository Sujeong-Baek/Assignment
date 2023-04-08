# https://school.programmers.co.kr/learn/courses/30/lessons/150370#
from collections import defaultdict
import datetime

def solution(today, terms, privacies):
    answer = [] 
    today=today.split('.')
    today=datetime.date(int(today[0]),int(today[1]),int(today[2]))
    for i, privacy in enumerate(privacies,1):
        day=calculator_date(terms, privacy)
        if today > datetime.date(day[0],day[1],day[2]):
            print(today,datetime.date(day[0],day[1],day[2]))
            answer.append(i)        
    return answer

#약관에해당하는 terms이용하여 날짜구하기
def calculator_date(terms, privacy):
    typ2month=defaultdict(int)
    privacy, typ =privacy.split(" ")
    privacy=privacy.split(".")
    for term in terms:
        t,month=term.split(" ")
        typ2month[t]=month

    DD=int(privacy[2])-1    
    MM=int(privacy[1])+int(typ2month[typ])    
    if DD==0:
        DD=28
        MM-=1
        
    YY=int(privacy[0])
    if MM>12:
        YY+=(MM-1)//12
        MM=(MM-1)%12+1  
    return YY,MM,DD