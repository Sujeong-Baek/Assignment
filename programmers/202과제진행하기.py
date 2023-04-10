# https://school.programmers.co.kr/learn/courses/30/lessons/176962#qna
def solution(plans):
    answer = []
    suspended=[]
    plans=cal_endtime(plans)    
    end_time=plans[0][2]
    for i in range(1,len(plans)):
        if plans[i][1]>=end_time:
            if not answer:
                answer.append(plans[i-1][0])
            answer.append(plans[i][0])
        elif plans[i][1]<end_time:
            suspended.append(plans[i-1][0])
        end_time=plans[i][2]
    
    while suspended:
        s=suspended.pop()
        answer.append(s)
    
    return answer


def cal_endtime(plans):
    plans = sorted(plans, key=lambda x: x[1])
    for i, (name, start, play_time) in enumerate(plans):
        start_h, start_m = map(int, start.split(':'))
        play_time=int(play_time)
        end_m = (start_m + play_time) % 60
        end_h = (start_h + (start_m + play_time) // 60) % 24
        plans[i][1] = start_h * 60 + start_m  # 분 단위로 변경
        plans[i][2] = end_h * 60 + end_m  # 분 단위로 변경
    return plans