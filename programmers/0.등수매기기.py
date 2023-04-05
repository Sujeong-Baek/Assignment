# https://school.programmers.co.kr/learn/courses/30/lessons/120882

def solution(score):
    average_list = []
    score_map={}
    num=1
    #평균 리스트 만들기 리버스로 정렬
    #map으로 점수2등수 점수가 같은것 나오면 등수
    for s in score:
        average_list.append(sum(s)/2)

    sorted_list=sorted(average_list, reverse=True)

    for average in sorted_list:
        if not average in score_map:
            score_map[average]=num              
        num+=1    
    return  [score_map[a] for a in average_list]