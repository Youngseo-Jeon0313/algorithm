# 1788
MOD = 1000000000

N = int(input())
if N==0:
    print(0)
elif N>0:
    print(1)
else:
    if N%2:
        print(1)
    else:
        print(-1)

DP = [0 for _ in range(1000000+1)]
DP[1]=1
for i in range(2,1000000+1):
    DP[i]=(DP[i-2]+DP[i-1])%MOD

abs_N = abs(N)
print(DP[abs_N]%MOD)
