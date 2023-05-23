# https://school.programmers.co.kr/learn/courses/30/lessons/152996
def cal_weight(w, weight2multi):
    if w in weight2multi:
        return weight2multi[w]    
    answer = []
    for distance in [2,3,4]:
        answer.append(w * distance)
    return answer

def solution(weights):
    answer = 0
    weight2multi = {}    
    for i, w1 in enumerate(weights[:-1], 1):
        weight2multi[w1] = cal_weight(w1, weight2multi)           
        for w2 in weights[i:]:
            weight2multi[w2] = cal_weight(w2, weight2multi)                
            if set(weight2multi[w1]) & set(weight2multi[w2]):
                answer += 1
    return answer