# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    s=s.split(" ")
    answer=[]
    for el in s:
        if el !="Z":
            answer.append(int(el))
        else:
            answer.pop()
    return sum(answer)
# 1 2 Z 3
# [1 3]