# https://school.programmers.co.kr/learn/courses/30/lessons/120863
def solution(polynomial):
    x=0
    n=0
    answer=''
    p_list=polynomial.split()
    for i in range(0,len(p_list),2):
        if p_list[i].isdigit():
            n+=int(p_list[i])
        else:
            if len(p_list[i])==1:
                x+=1
            else:
                x+=int(p_list[i][:-1])
    if x:
        if not x==1:
            answer+=str(x)+'x'
        else:
            answer+='x'
    if answer:
        if n:
            answer+=' + '+str(n)
    else:
        answer+=str(n)    
            
    return answer