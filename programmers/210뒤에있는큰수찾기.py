# https://school.programmers.co.kr/learn/courses/30/lessons/154539
def solution(numbers):
    answer=[-1 for _ in range(len(numbers))]
    number_index=[]
    for i, number in enumerate(numbers):
        while number_index and  numbers[number_index[-1]]<number:
            index=number_index.pop()
            answer[index]=number
        number_index.append(i)
    return answer