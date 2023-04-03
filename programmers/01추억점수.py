from collections import defaultdict

# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    answer = []
    name2yearning = create_name2yearning(name, yearning)
    for p in photo:                
        answer.append(add_photo_yearning(p,name2yearning))
    return answer

def create_name2yearning(name, yearning):
    name2yearning=defaultdict(int)
    for n, y in zip(name, yearning):
        name2yearning[n]=y
    return name2yearning


# ["may", "kein", "kain", "radi"] -> 19
def add_photo_yearning(p,name2yearning):
    total_photo_yearning=0
    for name in p:
        total_photo_yearning += name2yearning[name]
    return total_photo_yearning


# ["may", "kein", "kain", "radi"]
# [5, 10, 1, 3]


# 	[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

# output
# [19, 15, 6]