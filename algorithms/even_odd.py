# https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    answer = [0,0]
    for num in num_list:
        if not num%2:
            answer[0]+=1
        else:
            answer[1]+=1
    return answer