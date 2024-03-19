N = int(input())
S = input()
DP = [float('inf') for _ in range(N)]
DP[0]=0
for i in range(1,N):
    if S[i]=='B':
        for j in range(i-1,-1,-1):
            if S[j]=='J' and DP[j]!=float('inf'):
                DP[i]=min(DP[i],DP[j]+(i-j)**2)
    elif S[i]=='O':
        for j in range(i-1,-1,-1):
            if S[j]=='B' and DP[j]!=float('inf'):
                DP[i]=min(DP[i],DP[j]+(i-j)**2)
                
    elif S[i]=='J':
        for j in range(i-1,-1,-1):
            if S[j]=='O' and DP[j]!=float('inf'):
                DP[i]=min(DP[i],DP[j]+(i-j)**2)
if DP[N-1]==float('inf'):
    print(-1)
else:
    print(DP[N-1])