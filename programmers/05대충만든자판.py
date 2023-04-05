# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = [0]*len(targets)
    
    for i,target in enumerate(targets): 
        for t in target:#"A"
            if answer[i]==-1:
                continue
            index_list=check_index_list(t, keymap)
            key_count=check_minindex(t, index_list,keymap)
            if key_count!=-1:
                answer[i]+=(key_count+1)
            else:
                answer[i]=-1
    return answer

#targets의 문자열을 받아 존재하면 keymap 인덱스
def check_index_list(t, keymap):
    index_list=[]
    for i, key in enumerate(keymap):        
        if t in key:
            index_list.append(i)
    return index_list
    
#index_list에서 작은 위치 반환
#indexlist=> j작은것
def check_minindex(t, index_list,keymap):
    j_index=[]
    if index_list:
        for index in index_list:
            j_index.append(keymap[index].index(t))
        return min(j_index)
    return -1