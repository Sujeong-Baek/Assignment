# https://school.programmers.co.kr/learn/courses/30/lessons/120907
def solution(quiz):
    answer = []
    #quiz 배열 문자열 하나씩 쪼개기 
    #if구절로 +,-연산 =뒤에오는 숫자와 정답 비교하기
    #맞으면o 아니면 x
    for q in quiz:
        x, op, y, _, z =q.split()
        if op =="+":
            ans=int(x)+int(y)
        else:
            ans=int(x)-int(y)
        if ans==int(z):
            answer.append("O")
        else:
            answer.append("X")
    return answer

# X [연산자] Y = Z # q: "3 - 4 = -3"