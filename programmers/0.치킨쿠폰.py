# https://school.programmers.co.kr/learn/courses/30/lessons/120884
def solution(chicken):
    #1마리당 쿠폰 한장
    #10장 모으면 한마리 서비스
    #서비스치킨도 쿠폰 한장+10장나머지 쿠폰
    answer = 0
    service, coupon = divmod(chicken,10) 
    
    while service:
        answer+=service     
        chicken=coupon+service
        service,coupon = divmod(chicken,10)
    return answer
        