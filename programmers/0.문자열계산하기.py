# https://school.programmers.co.kr/learn/courses/30/lessons/120902
def solution(my_string):
    mr_list=my_string.split()
    answer=int(mr_list[0])
    
    for i in range(1,len(mr_list),2):
        if mr_list[i]=="+":
            answer+=int(mr_list[i+1])
        else:
            answer-=int(mr_list[i+1])
    return answer