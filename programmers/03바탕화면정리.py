# https://school.programmers.co.kr/learn/courses/30/lessons/161990

EMPTY = "."
FILE = "#"
#(1,6) (3,4)-> (1,3) (5,4) (3,8)->(5,8)
def solution(wallpaper):
    min_x=len(wallpaper) - 1
    min_y=len(wallpaper[0]) - 1
    max_x=0
    max_y=0
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == FILE:
                min_x=min(min_x,row)
                min_y=min(min_y,col)
                max_x=row
                max_y=max(max_y,col)
    return [min_x, min_y,max_x+1,max_y+1]

# [
# ".#...", (0,1)
# "..#..", (1,2)
# "...#."  (2,3)
# ] 

# [
# "....#", (0,4)
# ".#...", (1,1)
# "..#..", (2,2)
# "...#."  (3,3)
# ] >> (0, 1) -> (3,4) (0,1,4,5)
# (min(x), min(y)) -> (max(x) + 1,max(y) + 1)