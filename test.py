# 1987
R, C = map(int,input().split())
List = []
for _ in range(R):
    List.append(list(input()))

visited = [0 for _ in range(ord('Z')-ord('A'))]
answer = 0
dy,dx=[-1,1,0,0],[0,0,-1,1]
def dfs(row,col,temp_answer):
    #print(col,visited)
    global answer
    answer = max(answer, temp_answer)
    for i in range(4):
        ny,nx = row+dy[i], col+dx[i]
        if 0<=ny<R and 0<=nx<C:
            if not visited[ord(List[ny][nx])-ord('A')]:
                visited[ord(List[ny][nx])-ord('A')]=1
                dfs(ny,nx,temp_answer+1)
                visited[ord(List[ny][nx])-ord('A')]=0
    return

visited[ord(List[0][0])-ord('A')]=1
dfs(0,0,1)

print(answer)