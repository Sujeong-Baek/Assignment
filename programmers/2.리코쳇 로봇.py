# https://school.programmers.co.kr/learn/courses/30/lessons/169199
from collections import deque

def find_index(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                rx, ry = i, j
            if board[i][j] == 'G':
                gx, gy = (i, j)
    return rx, ry, gx, gy

def bfs(board, rx, ry, gx, gy):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()

def solution(board):
    rx, ry, gx, gy = find_index(board)
    return 