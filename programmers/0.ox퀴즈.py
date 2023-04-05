# https://school.programmers.co.kr/learn/courses/30/lessons/120907
def solution(quiz):
    answer = []
    #quiz 배열 문자열 하나씩 쪼개기 
    #if구절로 +,-연산 =뒤에오는 숫자와 정답 비교하기
    #맞으면o 아니면 x
    for q in quiz:
        q_list=q.split()        
        if q_list[1] =="+":
            ans=int(q_list[0])+int(q_list[2])
        elif q_list[1] =="-":
            ans=int(q_list[0])-int(q_list[2])
            
        if ans==int(q_list[-1]):
            answer+="O"
        else:
            answer+="X"
        
    return answer