# https://school.programmers.co.kr/learn/courses/30/lessons/120956
def solution(babbling):
    answer = 0

    babies=["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        found = True
        while bab and found:
            found = False
            for baby in babies:
                if baby==bab[:len(baby)]:
                    bab=bab[len(baby):]
                    found = True
        if not bab:
            answer += 1
    return answer         

# bayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaaya
# ayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaaya
# ayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaaya

def prefix(a, b):
    return a == b[:len(a)]
