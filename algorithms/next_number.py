# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    if common[1]-common[0]==common[2]-common[1]:
        return common[-1]+common[1]-common[0]
    return common[-1]*(common[1]/common[0])
    