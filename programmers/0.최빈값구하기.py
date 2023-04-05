# https://school.programmers.co.kr/learn/courses/30/lessons/120812
def solution(array):
    a_map={}
    answer=[]
    for a in array:
        if not a in a_map:
            a_map[a]=1
        else:
            a_map[a]+=1

    max_a=max(a_map.values())
    for key in a_map:
        if a_map[key]==max_a:
            answer.append(key)

    if len(answer)>1:
        return -1
    return answer[0]