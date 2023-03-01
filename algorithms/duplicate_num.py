# https://school.programmers.co.kr/learn/courses/30/lessons/120583

def solution(array, n):
    # return sum([num == n for num in array])
    answer = 0
    for num in array:
        if num == n:
            answer += 1
    return answer

# list comprehension

print([i for i in range(4)])
print([num == 2 for num in [1,2,3,4]])