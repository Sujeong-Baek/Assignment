"""shuffle()에서 랜덤하게 움직이기"""
import random

# sliding puzzle을 구현하는 과제입니다:)
# 아래는 과제가 완성된 후 동작하는 예시입니다.
# python sliding_puzzle.py 3 4
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# | 10 | |  5 | |  7 | | 11 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  9 | |  1 | |  2 | |  6 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
#        o----o o----o o----o
#        |    | |    | |    |
#        |  3 | |  8 | |  4 |
#        |    | |    | |    |
#        o----o o----o o----o

# What is your move> d
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# | 10 | |  5 | |  7 | | 11 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
#        o----o o----o o----o
#        |    | |    | |    |
#        |  1 | |  2 | |  6 |
#        |    | |    | |    |
#        o----o o----o o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  9 | |  3 | |  8 | |  4 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o

# What is your move> left
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# | 10 | |  5 | |  7 | | 11 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
# o----o        o----o o----o
# |    |        |    | |    |
# |  1 |        |  2 | |  6 |
# |    |        |    | |    |
# o----o        o----o o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  9 | |  3 | |  8 | |  4 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o

# What is your move> l
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# | 10 | |  5 | |  7 | | 11 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
# o----o o----o        o----o
# |    | |    |        |    |
# |  1 | |  2 |        |  6 |
# |    | |    |        |    |
# o----o o----o        o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  9 | |  3 | |  8 | |  4 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o

# What is your move> D
# o----o o----o        o----o
# |    | |    |        |    |
# | 10 | |  5 |        | 11 |
# |    | |    |        |    |
# o----o o----o        o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  1 | |  2 | |  7 | |  6 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  9 | |  3 | |  8 | |  4 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o

# What is your move> R
# o----o        o----o o----o
# |    |        |    | |    |
# | 10 |        |  5 | | 11 |
# |    |        |    | |    |
# o----o        o----o o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  1 | |  2 | |  7 | |  6 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  9 | |  3 | |  8 | |  4 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o

# What is your move> u
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# | 10 | |  2 | |  5 | | 11 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
# o----o        o----o o----o
# |    |        |    | |    |
# |  1 |        |  7 | |  6 |
# |    |        |    | |    |
# o----o        o----o o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  9 | |  3 | |  8 | |  4 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o

# What is your move>

# 놀이판을 만드는 함수입니다.
# 2차원의 list를 반환합니다
# make_board(2, 2) => [[1, 2], [3, 0]]
# make_board(4, 7) =>
# [[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14],
# [15, 16, 17, 18, 19, 20, 21],[22, 23, 24, 25, 26, 27, 0]]
def make_board(rows, cols):
    """놀이판을 만드는 함수로 2차원의 list를 반환합니다."""
    list_two=[]
    for i in range(0, rows*cols, cols):
        list_one=[]
        for j in range(i+1,i+1+cols):
            list_one.append(j)
        list_two.append(list_one)
    list_two[-1][-1]=0
    return list_two

def make_board2(rows, cols):
    """놀이판을 만드는 함수로 2차원의 list를 반환합니다."""
    board=[]
    for row in range(rows):
        board.append([row*cols + col + 1 for col in range(cols)])
    board[-1][-1] = 0
    return board

# lint
# pylint
# sql : standard query language
# 1 mike  123-4567
# 2 alice 345-6789


# 놀이판을 출력하는 함수입니다. 0은 빈칸을 나타냅니다.
# >>> display_board(make_board(2, 3))
# o----o o----o o----o
# |    | |    | |    |
# |  1 | |  2 | |  3 |
# |    | |    | |    |
# o----o o----o o----o
# o----o o----o
# |    | |    |
# |  4 | |  5 |
# |    | |    |
# o----o o----o
# >>> display_board(make_board(4, 4))
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  1 | |  2 | |  3 | |  4 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  5 | |  6 | |  7 | |  8 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
# o----o o----o o----o o----o
# |    | |    | |    | |    |
# |  9 | | 10 | | 11 | | 12 |
# |    | |    | |    | |    |
# o----o o----o o----o o----o
# o----o o----o o----o
# |    | |    | |    |
# | 13 | | 14 | | 15 |
# |    | |    | |    |
# o----o o----o o----o
# >>> display_board(make_board(3, 9))
# o----o o----o o----o o----o o----o o----o o----o o----o o----o
# |    | |    | |    | |    | |    | |    | |    | |    | |    |
# |  1 | |  2 | |  3 | |  4 | |  5 | |  6 | |  7 | |  8 | |  9 |
# |    | |    | |    | |    | |    | |    | |    | |    | |    |
# o----o o----o o----o o----o o----o o----o o----o o----o o----o
# o----o o----o o----o o----o o----o o----o o----o o----o o----o
# |    | |    | |    | |    | |    | |    | |    | |    | |    |
# | 10 | | 11 | | 12 | | 13 | | 14 | | 15 | | 16 | | 17 | | 18 |
# |    | |    | |    | |    | |    | |    | |    | |    | |    |
# o----o o----o o----o o----o o----o o----o o----o o----o o----o
# o----o o----o o----o o----o o----o o----o o----o o----o
# |    | |    | |    | |    | |    | |    | |    | |    |
# | 19 | | 20 | | 21 | | 22 | | 23 | | 24 | | 25 | | 26 |
# |    | |    | |    | |    | |    | |    | |    | |    |
# o----o o----o o----o o----o o----o o----o o----o o----o
def display_board(board):
    """놀이판을 출력하는 함수입니다. 0은 빈칸을 나타냅니다."""
    top_bottom = 'o----o'
    side = '|    |'
    ans = ""
    for i in board: # [1, 2, 3, 4]
    # for row in board: # [1, 2, 3, 4]
        if i[0]==0 :
            line = ["      ", "      ", "      ","      ","      "]
        else :
            number = f'|{str(i[0]):^4}|'
            line = [top_bottom,side,number,side,top_bottom]
        for j in i[1:]:
            if j==0:
                card = ["      ", "      ", "      ","      ","      "]
            else:
                number = f'|{str(j):^4}|'
                card = [top_bottom,side,number,side,top_bottom]
            line = [f"{l}{' '}{r}" for l,r in zip(line, card)]
        line = "\n".join(line)
        ans += line+"\n"
    print(ans[:-1])

# 클래스를 사용해봅시다
class Pos:
    """Pos 클래스를 사용해봅시다"""
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return f"Pos(row={self.row}, col={self.col})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other) == Pos and self.row == other.row and self.col == other.col

# 놀이판 board를 input 으로 받아서 빈칸의 위치를 Pos 로 리턴하는 함수입니다.
# >>> find_empty(make_board(2, 3))
# Pos(row=1, col=2)
# >>> find_empty(make_board(4, 4))
# Pos(row=3, col=3)
# >>> find_empty(make_board(3, 9))
# Pos(row=2, col=8)
def find_empty(board):
    """놀이판 board를 input 으로 받아서 빈칸의 위치를 Pos 로 리턴하는 함수입니다."""
    for i in enumerate(board):
        if 0 in i[1]:
            return Pos(i[0], i[1].index(0))
    return None

# >>> left = Pos(0, 1)
# >>> right = Pos(0, -1)
# >>> up = Pos(1, 0)
# >>> down = Pos(-1, 0)
# >>> b1 = make_board(2,3)
# >>> display_board(b1)
# o----o o----o o----o
# |    | |    | |    |
# |  1 | |  2 | |  3 |
# |    | |    | |    |
# o----o o----o o----o
# o----o o----o
# |    | |    |
# |  4 | |  5 |
# |    | |    |
# o----o o----o
# >>> make_move(b1, down)
# >>> display_board(b1)
# o----o o----o
# |    | |    |
# |  1 | |  2 |
# |    | |    |
# o----o o----o
# o----o o----o o----o
# |    | |    | |    |
# |  4 | |  5 | |  3 |
# |    | |    | |    |
# o----o o----o o----o
# >>> make_move(b1, right)
# >>> display_board(b1)
# o----o        o----o
# |    |        |    |
# |  1 |        |  2 |
# |    |        |    |
# o----o        o----o
# o----o o----o o----o
# |    | |    | |    |
# |  4 | |  5 | |  3 |
# |    | |    | |    |
# o----o o----o o----o

def make_move(board, pos):
    """pos를 받아서 board를 움직이기"""
    zero = find_empty(board)
    other = Pos(int(zero.row + pos.row), int(zero.col + pos.col))
    if other.row <0 or other.row>=len(board) or other.col <0 or other.col>=len(board[0]) :
        return False
    other_num = board[other.row][other.col]
    board[other.row][other.col] = 0
    board[zero.row][zero.col] = other_num
    return True

# make_move를 이용해서 iter만큼 board를 random하게 움직여주세요.
def shuffle(board, num):
    """make_move를 이용해서 iter만큼 board를 random하게 움직여주세요."""
    pos_s = [Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)]
    for _ in range(num):
        pos = pos_s[random.randrange(0,4)]
        while not make_move(board, pos):
            pos = pos_s[random.randrange(0,4)]
    return board

# 유저의 input을 Pos object로 변환하는 함수입니다
# empty 가 아닌 첫번째 글자를 확인해야 하고 invalid한 input에 대해서는 Pos(0,0)을 리턴합니다
# >>> str_to_move(" left ")
# Pos(row=0, col=1)
# >>> str_to_move("  Left ")
# Pos(row=0, col=1)
# >>> str_to_move("r")
# Pos(row=0, col=-1)
# >>> str_to_move("  UP")
# Pos(row=1, col=0)
# >>> str_to_move("  DN  ")
# Pos(row=-1, col=0)
# >>> str_to_move("  XYZ ")
# Pos(row=0, col=0)
# >>> str_to_move("")
# Pos(row=0, col=0)
def str_to_move(start):
    """유저의 input을 Pos object로 변환하는 함수입니다"""
    start = start.replace(" ", "").upper()
    if start[0] == "L":
        return Pos(0, 1)
    if start[0] == "R":
        return Pos(0, -1)
    if start[0] == "U":
        return Pos(1, 0)
    if start[0] == "D":
        return Pos(-1, 0)
    if not start[0] in "LRUD":
        return Pos(0, 0)
    return None

def play_game(rows, cols):
    """이제 게임을 해봅시다"""
    board = make_board(rows, cols)
    shuffle(board, 1000)
    while True:
        display_board(board)
        start = input("What is your move> ")
        if start == "quit":
            return
        move = str_to_move(start)
        make_move(board, move)

play_game(3,2)
