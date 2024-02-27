from collections import deque

# 2072
def bfs(board,row,col,color):
    visited=[[0 for _ in range(20)] for _ in range(20)]
    #위아래
    ans_1 = 1
    deq = deque([])
    deq.append([row,col])
    while deq:
        ny, nx = deq.popleft()
        visited[ny][nx]=1
        for dy,dx in [[-1,0], [1,0]]:
            if 1<=ny+dy<20 and 1<=nx+dx<20:
                if not visited[ny+dy][nx+dx] and board[ny+dy][nx+dx]==color:
                    visited[ny+dy][nx+dx]=1
                    ans_1+=1
                    deq.append([ny+dy,nx+dx])
    # 양옆
    ans_2 = 1
    deq = deque([])
    deq.append([row,col])
    while deq:
        ny, nx = deq.popleft()
        visited[ny][nx]=1
        for dy,dx in [[0,1], [0,-1]]:
            if 1<=ny+dy<20 and 1<=nx+dx<20:
                if not visited[ny+dy][nx+dx] and board[ny+dy][nx+dx]==color:
                    visited[ny+dy][nx+dx]=1
                    ans_2+=1
                    deq.append([ny+dy,nx+dx])  
    # 오른쪽 대각선
    ans_3 = 1
    deq = deque([])
    deq.append([row,col])
    while deq:
        ny, nx = deq.popleft()
        visited[ny][nx]=1
        for dy,dx in [[1,1], [-1,-1]]:
            if 1<=ny+dy<20 and 1<=nx+dx<20:
                if not visited[ny+dy][nx+dx] and board[ny+dy][nx+dx]==color:
                    visited[ny+dy][nx+dx]=1
                    ans_3+=1
                    deq.append([ny+dy,nx+dx])  
    # 왼쪽 대각선
    ans_4 = 1
    deq = deque([])
    deq.append([row,col])
    while deq:
        ny, nx = deq.popleft()
        visited[ny][nx]=1
        for dy,dx in [[-1,1], [1,-1]]:
            if 1<=ny+dy<20 and 1<=nx+dx<20:
                if not visited[ny+dy][nx+dx] and board[ny+dy][nx+dx]==color:
                    visited[ny+dy][nx+dx]=1
                    ans_4+=1
                    deq.append([ny+dy,nx+dx])  
    if (ans_1 == 5 or ans_2 ==5 or ans_3 ==5 or ans_4 ==5):
        return True
    return False

N = int(input()) # 좌표는 19x19
BOARD = [[-1 for _ in range(20)] for _ in range(20)]
for i in range(N): # 홀수 흑, 짝수 백
    row,col = map(int,input().split())
    #일단 넣고
    BOARD[row][col]=i%2
    if bfs(BOARD,row,col,i%2): 
        print(i+1); exit()
print(-1)
    