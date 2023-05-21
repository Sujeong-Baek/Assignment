# https://school.programmers.co.kr/learn/courses/30/lessons/181188
def solution(targets):
    targets=sorted(targets)
    count = 0
    interception = {'s' : 0, 'e' : 0}
    for s, e in targets:
        if interception['e'] <=s:
            count += 1
            interception = {'s' : s, 'e' : e}
        else:
            interception = {'s' : max(interception['s'], s), 'e' : min(interception['e'], e)}
    return count