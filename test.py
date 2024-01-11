### 메모리초과 -> 굳이 큐 안에 여러 정보를 넣지 말자. 더 최적화하는 방법 찾기 !

from collections import deque

# 공주님을 구해라 !
N,M,T = map(int,input().split())
List = []
for _ in range(N):
    List.append(list(map(int,input().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]
#2가 있는 곳 - 그람
q = deque()
q.append([0,0]) #x,y

dx, dy = [-1,1,0,0], [0,0,-1,1]
visited[0][0]=1

ans = float('inf')

while q:
    now_x, now_y = q.popleft()
    for i in range(4):
        nx, ny = now_x+dx[i], now_y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M: continue
        if visited[nx][ny]: continue
        if List[nx][ny]==0 : #그냥 칸
            visited[nx][ny]=visited[now_x][now_y]+1
            q.append([nx, ny])
        elif List[nx][ny]==2 : #그람
            visited[nx][ny] = visited[now_x][now_y] + 1
            ans = min(ans, visited[now_x][now_y]+1+(N-1-nx)+(M-1-ny)-1)
            q.append([nx, ny])

# print(visited)
if visited[N-1][M-1]-1>=0:
    ans = min(ans, visited[N-1][M-1]-1)
if ans<=T :
    print(ans)
else:
    print("Fail")