import sys
input = sys.stdin.readline

# 2610

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]


def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def find(a):
    if a == parent[a]: #여기 잊지 말 것 !!
        return a
    parent[a] = find(parent[a])
    return parent[a]

adj = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    union(a,b)
for i in range(N+1):
    find(i)

dict = {}
answer = set()
for i in range(1,N+1):
    answer.add(parent[i])
    if parent[i] not in dict.keys():
        dict[parent[i]]=[i]
    else:
        dict[parent[i]].append(i)

print(len(answer))
ans = []
#print(adj)
for key, values in dict.items():
    DP = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
    # 여기에서 이제 그냥 빡구현
    for i in values:
        DP[i][i]=0
        for j in adj[i]:
            DP[i][j]=1
    for k in values:
        for i in values:
            for j in values:
                if DP[i][j]>DP[i][k]+DP[k][j]:
                    DP[i][j]=DP[i][k]+DP[k][j]
    temp_ans = ''; min_value = float('inf')
    #print(DP)
    for i in values:
        temp_max = 0
        for j in DP[i]:
            if j!=float('inf'): 
                temp_max = max(temp_max,j)
        if min_value>temp_max:
            min_value = temp_max; temp_ans = i
    ans.append(temp_ans)
ans.sort()
for i in ans:
    print(i)