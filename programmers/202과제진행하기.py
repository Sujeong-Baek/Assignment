# https://school.programmers.co.kr/learn/courses/30/lessons/176962#qna
def solution(plans):
    answer = []
    plans=sorted(plans, key=lambda x: x[1])
    for plan in plans:
        plan[1]=int(plan[1][:2])*60+int(plan[1][3:])
        plan[2]=int(plan[2])
        
    suspended=[plans[0]]
    now=plans[0][1]
    for plan in plans[1:]:
        while suspended and now+suspended[-1][2]<=plan[1]:
            now+=suspended[-1][2] 
            answer.append(suspended.pop()[0])
        if suspended:
            suspended[-1][2]-=plan[1]-now
        suspended.append(plan)
        now=plan[1]

    while suspended:
        answer.append(suspended.pop()[0])
        
    return answer