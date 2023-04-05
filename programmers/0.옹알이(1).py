# https://school.programmers.co.kr/learn/courses/30/lessons/120956
def solution(babbling):
    answer = 0

    baby_list=["aya", "ye", "woo", "ma"]
    talk_list=[]
    
    for bab in babbling:
        for baby in baby_list:
            bab=bab.replace(baby,"1")
        talk_list.append(bab)
    
    for talk in talk_list:
        if talk.isdigit():
            answer+=1
    return answer