from collections import deque
N = int(input())
arr = [[0,0]for _ in range(N)]
answer = float('inf')

for i in range(N-1):
    a, b = map(int,input().split())
    arr[i][0]=a; arr[i][1]=b;

K = int(input())
q = deque([]) 
q.append((0,0,0)) #node, flag, score

while q:
    node, flag, score = q.popleft()
    if node==N-1:
        answer = min(answer, score)
    if node+1<N:
        q.append((node+1, flag, score+arr[node][0]))
    if node+2<N:
        q.append((node+2, flag, score+arr[node][1]))
    if node+3<N and flag==0:
        q.append((node+3, 1, score+K))
print(answer)