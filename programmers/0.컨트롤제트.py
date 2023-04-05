# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    s_list = s.split()
    answer=0
    for i in range(len(s_list)):
        if s_list[i]=='Z':
            answer-=int(s_list[i-1])
        else:
            answer+=int(s_list[i])
    return answer