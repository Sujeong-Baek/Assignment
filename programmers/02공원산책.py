# https://school.programmers.co.kr/learn/courses/30/lessons/172928
def solution(park, routes):
    r, c =find_S_index(park)
    return move_routes(r,c,routes, park)


# ["SOO","OOO","OOO"] -> [0,0]
def find_S_index(park):
    for r in range(len(park)):
        for c in range(len(park[r])):
            if park[r][c]=="S":
                return [r,c]

# 0,0 ,["E 2","S 3","W 1"]->[0,0]
def move_routes(r, c, routes, park):
    op2drdc = {"E": (0, 1), "W":(0,-1), "S":(1,0), "N":(-1,0)}
    R = len(park) # 3
    C = len(park[0]) # 3
    for route in routes: # route: "E 2"
        op, num = route.split() # "E", "2"
        num = int(num) # 2
        dr, dc = op2drdc[op] # 0, 1
        nr=r # 0
        nc=c # 0
        for _ in range(num):
            if 0 > (nr+dr) or (nr+dr) >= R or 0 > (nc+dc) or (nc + dc)>= C or park[(nr+dr)][(nc+dc)] == 'X':
                nr, nc = r, c
                break
            else:
                nr+=dr
                nc+=dc
        r, c = nr, nc
    return[nr,nc]
# print(move_routes(0,0,["E 2"],["SOX","OXX","OOO"])) -> [0,0]
# print(move_routes(0,0,["E 2"],["SXO","OXX","OOO"])) -> [0,0]
# print(move_routes(0,0,["E 4"],["SOO","OXX","OOO"])) -> [0,0]
# print(move_routes(0,0,["E 2"],["OOO","SXX","OOO"])) -> [1,0]


# input
# [
# "SOO",
# "OOO",
# "OOO"]
# ["E 2","S 2","W 1"]
# 
# output
# [2,1]