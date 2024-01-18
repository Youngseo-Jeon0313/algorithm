#리코챗 로봇

from collections import deque

def solution(board):
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    goal = []
    deq = deque([]) #y,x
    visited=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='G':
                goal = [i,j]
            elif board[i][j]=='R':
                deq.append([i,j,1])
                visited[i][j]=1
    while deq:
        #print(deq)
        y,x,step = deq.popleft()
        for i in range(4):
            ny, nx = y, x
            while True:
                ny = ny+dy[i]; nx = nx+dx[i]
                if 0<=nx<len(board[0]) and 0<=ny<len(board) and board[ny][nx]=='D': #만나게 되면 #만나게 되면
                    ny-=dy[i]; nx-=dx[i]
                    break
                elif nx<0 or nx>=len(board[0]) or ny<0 or ny>=len(board):
                    ny-=dy[i]; nx-=dx[i]
                    break
            if not visited[ny][nx]:
                visited[ny][nx]=step+1
                deq.append([ny,nx,step+1])
    print(visited)
    if visited[goal[0]][goal[1]]>0:
        answer = visited[goal[0]][goal[1]]-1
    else:
        answer = -1
    return answer