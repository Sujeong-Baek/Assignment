# https://school.programmers.co.kr/learn/courses/30/lessons/120812
from collections import Counter

def solution(array):
    if len(array)==1:
        return array[0]
    counter = Counter(array)
    a, b = counter.most_common(2)
    return a[0] if a[-1]!=b[-1] else -1


counter = Counter([1, 2, 2,2,3, 3, 3, 4])
print(counter.most_common(2))