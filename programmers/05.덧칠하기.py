# https://school.programmers.co.kr/learn/courses/30/lessons/161989
def solution(n, m, section):
    answer = 0
    # n길이만큼 0리스트 만들기
    #위 리스트에 section 원소를 section-1인덱스에 넣기
    #숫자가 0이 아닌 곳부터 시작하여 m만큼의 길이를 (0이 아닌 숫자만 0으로 바꾸기)
    #m만큼의 길이는 리스트의 범위를 벗어나면 안됨
    
    wall=[0]*n  
    for num in section:
        wall[num-1]=num        
    for i, w in enumerate(wall):
        if w!=0 :
            if i<=len(wall):                   
                wall[i:i+m:]=[0]*m
                answer+=1    
   
    return answer