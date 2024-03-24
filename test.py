N = int(input())
List = []
for _ in range(N):
    List.append(list(map(int,input().split())))
DP = [[0 for _ in range(N)] for _ in range(N)]
DP[0][0]=List[0][0]
for i in range(1,N):
    for j in range(i+1):
        if j>0:
            DP[i][j]=max(DP[i-1][j-1]+List[i][j],DP[i-1][j]+List[i][j])
        else:
            DP[i][j]=DP[i-1][j]+List[i][j]
print(max(DP[-1]))