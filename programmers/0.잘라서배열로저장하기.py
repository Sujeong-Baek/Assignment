# https://school.programmers.co.kr/learn/courses/30/lessons/120913
def solution(my_str, n):
    
    return  [my_str[i:i+n] for i in range(0,len(my_str),n)]