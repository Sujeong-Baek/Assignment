# https://school.programmers.co.kr/learn/courses/30/lessons/120875
def solution(dots):   
    m=[]

    #a-b, a-d, a-d, b-c, b-d, c-b
    for i in range(len(dots)-1):
        for j in range(i+1,len(dots)):
            m.append((dots[i][1]-dots[j][1])/(dots[i][0]-dots[j][0]))

    # [a-b, c-d],[a-c, b-d],[a-d, b-c]       
    for i in range(3):
        if m[i] == m[len(m)-1-i]:
            return 1
    return 0