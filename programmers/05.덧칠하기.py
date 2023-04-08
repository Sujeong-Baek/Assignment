# https://school.programmers.co.kr/learn/courses/30/lessons/161989
def solution(n, m, section):
    answer = 0
    # n길이만큼 0리스트 만들기
    #위 리스트에 section 원소를 section-1인덱스에 넣기
    #숫자가 0이 아닌 곳부터 시작하여 m만큼의 길이를 (0이 아닌 숫자만 0으로 바꾸기)
    #m만큼의 길이는 리스트의 범위를 벗어나면 안됨
    
    max_painted = 0
    for s in section:
        if max_painted<s:
            max_painted=s+m-1
            answer+=1
    return answer


    # 8	4	[2, 3, 6]	2
    # 1 2 3 4 5 6 7 8
    #   X X X X
    #           X X X X 
    # max_painted = 0
    # max_painted = 2 + 4 - 1 = 5
    # max_painted = 6 + 4 - 1 = 9


    # i 번째를 돌 때 i-1번까지는 이미 다 칠해졌다고 가정하고
    # i 번째를 칠하면 i+m-1 번째까지는 칠해진다.
    # max_painted = i + m - 1
