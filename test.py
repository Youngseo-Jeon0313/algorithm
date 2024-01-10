# 우유도시
# 0까지 | 1까지 | 2까지
N=int(input())
List = []
for _ in range(N):
    List.append(list(map(int,input().split())))
DP = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

# DP[0][0]에만 우선적으로 적용해보자.
# init -> X 그냥 아래에서 적용


for i in range(N):
    for j in range(N):
        if List[i][j]==0:
            DP[i][j][0]=max(DP[i][j][0],1)
        if i>0: #왼쪽 가능
            val = List[i][j]
            DP[i][j][val] = max(DP[i][j][val], DP[i-1][j][val])
            if DP[i-1][j][(val-1+3)%3] > 0 :
                DP[i][j][val] = max(DP[i][j][val], DP[i-1][j][(val-1+3)%3] +1)
            DP[i][j][(val+1)%3] = max(DP[i][j][(val+1)%3],DP[i-1][j][(val+1)%3] )
            DP[i][j][(val+2)%3] = max(DP[i][j][(val+2)%3],DP[i-1][j][(val+2)%3] )
        if j>0: #위쪽 가능
            val = List[i][j]
            DP[i][j][val] = max(DP[i][j][val],DP[i][j-1][val])
            if DP[i][j-1][(val-1+3) % 3] > 0:
                DP[i][j][val] = max(DP[i][j][val], DP[i][j - 1][(val - 1 + 3) % 3] + 1)
            DP[i][j][(val + 1) % 3] = max(DP[i][j][(val + 1) % 3], DP[i][j-1][(val + 1) % 3])
            DP[i][j][(val + 2) % 3] = max(DP[i][j][(val + 2) % 3], DP[i][j-1][(val + 2) % 3])
# for i in DP:
#     print(i)

print(max(DP[-1][-1]))