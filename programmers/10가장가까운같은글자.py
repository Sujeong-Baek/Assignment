# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer=[]
    letter2idx = {}
    for idx, letter in enumerate(s):
        if letter not in letter2idx:
            letter2idx[letter]==idx
            answer.append(-1)
        else:
            answer.append(idx-letter2idx[letter])
            letter2idx[letter]==idx
    return answer

# count, index, min(lst), max(lst), find, replace 이런건 안씀

# banana
# b : -1, b -> 1
# a : -1, b -> 1, a -> 2
# n : -1, b -> 1, a -> 2, n -> 3
# a : 2, b -> 1, a -> 4 - 2 = 2, n -> 3
# n : 2, b -> 1, a -> 4, n -> 5
# a : 2, b -> 1, a -> 6, n -> 5
# banan
# banana
# letter2num