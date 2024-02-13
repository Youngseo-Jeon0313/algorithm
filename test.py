# [BFS] 퍼즐 조각 채우기 - 삼성 구현 느낌의 문제

from collections import deque
'''
회전 ㅇ / 뒤집기 x
game_board와 table 모양을 1:1 대응시켜서 비교하자.
'''
dx, dy =[-1,1,0,0], [0,0,-1,1]

def puzzle_tuning(puzzle):
    min_x = float('inf')
    min_y = float('inf')
    for i in puzzle:
        min_x = min(min_x, i[0])
        min_y = min(min_y, i[1])
    for j in puzzle:
        j[0]-=min_x
        j[1]-=min_y
    return puzzle

def bfs(board, flag): # board -> puzzles
    N = len(board)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    puzzles = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j]==flag:
                puzzle = [[i,j]]
                deq = deque([(i,j)])
                while deq:
                    y,x = deq.popleft()
                    visited[y][x]=1
                    for k in range(4):
                        ny = y+dy[k]; nx = x+dx[k]
                        if 0<=ny<N and 0<=nx<N:
                            if not visited[ny][nx] and board[ny][nx]==flag:
                                deq.append((ny,nx)); puzzle.append([ny,nx])
                puzzles.append(puzzle_tuning(puzzle))
    return puzzles

def turn_90(board):
    temp =[]
    N=sorted(board)[-1][0]
    for i in board:
        temp.append([i[1],N-i[0]])
    return temp

def solution(game_board, table):
    answer = 0
    A = bfs(game_board, 0)
    B = bfs(table, 1)
    check_A = [0 for _ in range(len(A))]
    check_B = [0 for _ in range(len(B))]
    for a in range(len(A)):
        for b in range(len(B)):
            if check_A[a] or check_B[b]: continue
            a_ = A[a]
            b_ = B[b]
            for c in range(4):
                b_=turn_90(b_)
                if sorted(a_)==sorted(b_):
                    check_A[a]=1
                    check_B[b]=1
                    answer+=len(b_)
                    break
    return answer