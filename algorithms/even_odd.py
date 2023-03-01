# https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    even = odd = 0
    for num in num_list:
        if not num%2:
            even +=1
        else:
            odd +=1
    return [even, odd]