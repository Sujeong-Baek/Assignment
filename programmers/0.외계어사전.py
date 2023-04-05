# https://school.programmers.co.kr/learn/courses/30/lessons/120869
def solution(spell, dic):

    spell.sort()

    for d in dic:
        if spell==sorted(d):            
            return 1       
    return 2