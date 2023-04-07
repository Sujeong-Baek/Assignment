# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer=[]
    for i, el in enumerate(s,1):
        if s[:i].count(el)==1: 
            answer.append(-1)  
        else:#i의 el을 제외, reverse하여 처음에나온 el과 같은 문자열의index
            answer.append(s[i-2::-1].index(el)+1)            
    return answer