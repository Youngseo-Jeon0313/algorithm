**PG 리코챗 로봇**
```python
from collections import *
dx=[-1,1,0,0]
dy=[0,0,1,-1]
 
def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0]) ##배열 크기를 나중에 많이 따져야 하니까 따로 변수 할당
    q = deque()
    dist = [[987654321 for _ in range(M)] for _ in range(N)]
    
    # 로봇(R)의 시작 위치를 찾아 큐에 추가
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i,j,0))
                dist[i][j] = 0
        if q:
            break
            
    while q:
        x,y,c = q.popleft()
        
        # 목표 지점(G)에 도착한 경우 이동 횟수 반환
        if board[x][y] == 'G':
            return c
        
        # 네 방향으로 이동할 수 있는 경우 탐색
        for i in range(4):
            n_x = x
            n_y = y
            
            # 해당 방향으로 미끄러지며 이동 가능한 위치 찾기
            while 0<=n_x+dx[i]<N and 0<=n_y+dy[i]<M and board[n_x+dx[i]][n_y+dy[i]] != 'D':
                n_x += dx[i]
                n_y += dy[i]
            
            # 이전에 해당 위치에 도달한 적이 없거나, 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우
            if dist[n_x][n_y] > c+1: #--> 여기에서 흔들리지 말자 ! 다익스트라 쓸 필요없이 이 경우도 그냥 큐에 넣어주면 됨
                dist[n_x][n_y] = c+1
                q.append((n_x,n_y,c+1))
    
    # 목표 지점에 도착할 수 없는 경우 -1 반환
    return -1
```

**프로그래머스 모두 0으로 만들기**
```python
import sys

sys.setrecursionlimit(300000)

'''
끝에 도달하면 ? -> 자기를 0으로 만들기 위해 부모에게 자기를 더해야 함.
그럼 각각의 노드는 무엇을 반환해야 해? -> 자신의 값을 반환
정답은 그 반환하는 전체 횟수가 중요함 -> abs(더하거나 빼는 행위의 값)

'''

answer = 0


def solution(a, edges):
    global answer
    if sum(a) != 0: return -1
    adj = [[] for _ in range(len(a))]
    for i in edges:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
    visited = [0 for _ in range(len(a))]

    def dfs(node):
        global answer
        visited[node] = 1
        temp = 0
        for i in adj[node]:
            if not visited[i]:
                check = dfs(i)
                a[node] += check
                answer += abs(check)
                # print(check)

        return a[node]

    # print(a)
    dfs(0)
    return answer
```

### BOJ 1991
전위 중위 후위
```
import sys
input = sys.stdin.readline

# 입력
n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]

# 전위 순회
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right

# 중위 순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right

# 후위 순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root

# 출력
preorder('A')
print()
inorder('A')
print()
postorder('A')
```