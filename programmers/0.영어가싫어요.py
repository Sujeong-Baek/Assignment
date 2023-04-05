# https://school.programmers.co.kr/learn/courses/30/lessons/120894
def solution(numbers):
    number=[ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, n in enumerate(number):
        numbers=numbers.replace(str(n),str(i))
    return int(numbers)