# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    els= ''
    answer=[]
    for el in s:
        if not el in els: 
            els+=el
            answer.append(-1)
        else:
            answer.append(len(els)-els.index(el))
            els=els.replace(el,' ')
            els+=el
    return answer