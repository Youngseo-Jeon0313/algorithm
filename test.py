'''
BFS? 다익스트라?
0인 곳을 우선적으로 도는 것이 좋다. 
그러다가 (N, M) 목적지에 다다르면 끝 !
'''

import heapq

dx, dy = [0,0,-1,1], [-1,1,0,0]

N, M = map(int,input().split())
List = []
for _ in range(M):
    List.append(list(input()))

for i in range(M):
    for j in range(N):
        List[i][j]=int(List[i][j])

hq = []
heapq.heapify(hq)
dist = [[float('inf') for _ in range(N)] for _ in range(M)]
heapq.heappush(hq, [List[0][0],List[0][0],0,0]) #벽 부순 갯수, 그 방의 상태, y,x,
dist[0][0]=List[0][0]
while hq:
    #print(dist)
    count, status, y, x = heapq.heappop(hq)
    if y==M-1 and x==N-1: 
        print(dist[M-1][N-1]);exit()
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<M and 0<=nx<N:
            if dist[ny][nx]>dist[y][x]+List[ny][nx]:
                dist[ny][nx]=dist[y][x]+List[ny][nx]
                heapq.heappush(hq, [dist[ny][nx], List[ny][nx],ny, nx])
    
print(dist[M-1][N-1])