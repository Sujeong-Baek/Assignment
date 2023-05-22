# https://school.programmers.co.kr/learn/courses/30/lessons/150370
from collections import defaultdict

def solution(today, terms, privacies):
    answer = [] 
    today_num =  date2num(today)

    term2month = defaultdict(int)
    for term in terms:
        t, month = term.split()
        term2month[t] = int(month)
        
    for i, privacy in enumerate(privacies, 1):
        date, term = privacy.split()
        month = term2month[term]
        if today_num >= calculator_date(month, date): 
            answer.append(i)        
    return answer if answer else -1

def date2num(date):
    year, month, day = date.split('.')
    return (int(year)*12 + int(month))*28 + int(day)


def calculator_date(month, date):   
    return date2num(date) + 28*month