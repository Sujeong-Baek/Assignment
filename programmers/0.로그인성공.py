# https://school.programmers.co.kr/learn/courses/30/lessons/120883
def solution(id_pw, db):
    for i in range(len(db)):        
        if id_pw == db[i]:
            return "login"
        elif id_pw[0]==db[i][0]:
            return "wrong pw"
    return "fail"