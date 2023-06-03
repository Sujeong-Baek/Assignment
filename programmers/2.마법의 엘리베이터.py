# https://school.programmers.co.kr/learn/courses/30/lessons/148653
def solution(storey):
    answer = 0

    while storey:
        units = storey % 10  
        if units > 5:
            answer += (10 - units)
            storey += 10
        elif units < 5:
            answer += units    
        else:
            if (storey//10)%10 >= 5:
                storey += 10
            answer+=units
        storey //= 10
    return answer