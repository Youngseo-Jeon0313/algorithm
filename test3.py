# 2229
# step DP

N = int(input())
List = list(map(int,input().split()))
DP = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i,N):
        DP[i][j]=abs(List[i]-List[j])
# print(DP)
for step in range(N): 
    for i in range(N-step):
        for j in range(i,i+step):
            #print(step,i,j)
            DP[i][i+step]=max(DP[i][i+step],DP[i][j]+DP[j+1][i+step])

print(DP[0][N-1])