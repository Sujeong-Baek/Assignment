# https://school.programmers.co.kr/learn/courses/30/lessons/120822


def solution(my_string):
    if len(my_string)==1:
        return my_string[-1]
    return my_string[-1]+solution(my_string[:-1])

