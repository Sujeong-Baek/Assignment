# https://school.programmers.co.kr/learn/courses/30/lessons/160586
def solution(keymap, targets):
    answer = []
    letter2num = create_letter2num(keymap)
    for target in targets:
        count=0
        for t in target: # target: "ABCD"
            if t in letter2num:
                count+=letter2num[t]
            else:
                count= -1
                break
        answer.append(count)
    return answer

def create_letter2num(keymap): # ["ABACD", "BCEFD"]
    letter2num = {}
    for key in keymap: # key: "ABACD"    
        for i,k in enumerate(key,1):
            if not k in letter2num:
                letter2num[k]=i
            elif letter2num[k] > i:
                letter2num[k]=i
    return letter2num

# ["ABACD", "BCEFD"]
# A -> 1
# B -> 1
# C -> 2
# D -> 5
# E -> 3
# F -> 4

# keymap -> letter2num
# A -> 1
# B -> 1
# C -> 2
# D -> 5
# E -> 3
# F -> 4
