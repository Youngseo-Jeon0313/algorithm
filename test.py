import sys
input = sys.stdin.readline

# 10971 외판원 순회 2
'''
어느 한 도시에서 출발해 N 개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로
-> 어차피 0, 1, 2, 3 을 거치니까 결국 0부터 해도 ㄱㅊ!
'''
N = int(input())
answer = float('inf')
List = []
for _ in range(N):
    List.append(list(map(int,input().split())))


def dfs(depth, node, cost, start): 
    global answer
    if depth==N-1 and List[node][start]>0:
        answer = min(answer, cost+List[node][start])
    for i in range(N):
        if not visited[i] and List[node][i]>0:
            visited[i]=1
            dfs(depth+1, i, cost+List[node][i], start)
            visited[i]=0


#시작
for start in range(N):
    visited = [0 for _ in range(N)]
    visited[start]=1
    dfs(0, start, 0, start)
    visited[start]=0

print(answer)