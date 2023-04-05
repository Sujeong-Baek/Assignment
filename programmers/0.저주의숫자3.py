# https://school.programmers.co.kr/learn/courses/30/lessons/120871
def solution(n):
  
    #3의 배수와 숫자3이 없는 숫자나열들 중에
    #n번째로 가리키는 것
    count=0
    number=0
    while count<n:
        number+=1
        if number%3==0 or "3" in str(number):
            continue
        count+=1

    return number