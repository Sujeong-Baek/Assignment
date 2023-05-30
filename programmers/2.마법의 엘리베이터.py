# https://school.programmers.co.kr/learn/courses/30/lessons/148653
def solution(storey):
    answer = 0

    while storey:
        units = storey % 10  
        if units >= 5:
            answer += (10 - units)
            storey += 10
        else:
            answer += units    
            
        storey //= 10
    return answer