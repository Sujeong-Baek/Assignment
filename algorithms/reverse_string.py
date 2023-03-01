# https://school.programmers.co.kr/learn/courses/30/lessons/120822


def solution(my_string):
    if len(my_string)==1:
        return my_string[-1]
    return my_string[-1]+solution(my_string[:-1])

# recursive vs iterative

# 'abcd'
# d -> c -> b -> a
def solution2(my_string):
    answer=''
    for idx in range(len(my_string)-1, -1, -1):
        answer+=my_string[idx]
    return answer

print(solution2("abcd"))