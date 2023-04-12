# https://school.programmers.co.kr/learn/courses/30/lessons/176962#qna
def solution(plans):
    answer = []
    plans = int_plans(plans)
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

# plans의 원소는 [name, start, playtime]의 구조로 이루어져 있습니다.
def int_plans(plans):
    answer = []
    for name, start, playtime in sorted(plans, key=lambda x: x[1]): #  ["music", "12:20", "40"],
        start_h, start_m=map(int, start.split(":"))
        answer.append([name,start_h*60+start_m,int(playtime)])
    return answer