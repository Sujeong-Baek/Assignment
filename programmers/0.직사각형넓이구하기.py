# https://school.programmers.co.kr/learn/courses/30/lessons/120860
def solution(dots):
    dots.sort()
    return abs(dots[0][1]-dots[1][1])*abs(dots[0][0]-dots[3][0])