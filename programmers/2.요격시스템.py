# https://school.programmers.co.kr/learn/courses/30/lessons/181188
def solution(targets):
    targets=sorted(targets)
    count = 0
    min_end= 0
    for s, e in targets:
        if min_end <= s:
            count += 1
            min_end = e
        else:
            min_end =  min(min_end, e)
    return count