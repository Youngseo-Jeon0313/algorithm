**BOJ 12978 트리 DP**


**BOJ 1949**

```python
import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    visited[n]=1
    DP[n][1]=List[n]
    for i in node[n]:
        if visited[i]: continue
        dfs(i) #해당 노드 처리
        #
        DP[n][0]+=max(DP[i][0],DP[i][1])#주변꺼에서 아닌 곳, 또는 주변꺼에서 맞는 곳
        DP[n][1]+=DP[i][0]
        
N=int(input())
List=list(map(int,input().split()))
List=[0]+List
node=[[] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    node[a].append(b)
    node[b].append(a)
DP=[[0 for _ in range(2)] for _ in range(N+1)]

dfs(1)
# print(DP)
print(max(DP[1]))
```

**BOJ 12978**
```python
'''
완전탐색이라면
2**N이 가능

하지만
특정한 i번째 노드를 루트로 하는 서브 트리에 대해서 i번째 루트 노드를 포함했을 때와 포함하지 않았을 때 중 조건에 맞는 답을 정의할경우
TREE DP 유력하다.
부모 노드를 계속해서 갱신해 감
'''

from sys import setrecursionlimit
setrecursionlimit(10**5)

def dfs(n):
    visited[n] = 1
    for i in adj[n]:
        if visited[i]:
            continue # 이미 온 곳
        dfs(i)  # 해당 노드 처리
        DP[n][1] += min(DP[i][0], DP[i][1])
        DP[n][0] += DP[i][1]
    return ## return 문 주의 !!! 

N = int(input())
adj = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
DP = [[0,1] for _ in range(N + 1)] # 0-경찰서x, 1-경찰서o

dfs(1)
# print(DP)
print(min(DP[1]))
```