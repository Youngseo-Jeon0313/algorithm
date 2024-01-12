#11057 파이썬
N = int(input())
ans = 0
DP = [[0 for _ in range(10)] for _ in range(1000)]
#init
for i in range(1000):
    for j in range(10):
        if i==0:
            DP[i][j]=1
        if j==0:
            DP[i][j]=1

for i in range(1, 1000):
    for j in range(1, 10):
        DP[i][j]=DP[i-1][j]+DP[i][j-1]


print(sum(DP[N-1])%10007)