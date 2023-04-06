# https://school.programmers.co.kr/learn/courses/30/lessons/120894
def solution(numbers):
    strnums=[ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer=''
    while numbers:
        for i, strnum in enumerate(strnums):
            if strnum==numbers[:len(strnum)]:
                numbers=numbers[len(strnum):]
                answer+=str(i)
    return int(answer)