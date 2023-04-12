# https://school.programmers.co.kr/learn/courses/30/lessons/172927

# [1,2,3]
# [1,3,2]
# [2,1,3]
# [2,3,1]
# [3,1,2]
# [3,2,1]

def produce(lst, prefix):
    if not lst:
        yield prefix
        return
    for i, el in enumerate(lst):
        yield from produce(lst[:i] + lst[i+1:], prefix + [el])

for combination in produce([1,2,3], []):
    print(combination)

# [1,3,2]
# [다이아, 철,철,철,돌,돌]


# lst[:0] + lst[1:] -> produce([2,3], [1])
# lst[:1] + lst[2:] -> produce([1,3], [2])
# lst[:2] + lst[3:] -> produce([1,2], [3])

