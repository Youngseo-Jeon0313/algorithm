'''
ABCDE
(A)(BCDE)
(AB)(CDE)
(ABC)(DE)
(ABCD)(E)

ANS 배열 따로 갱신
'''

#11066
T=int(input())
for _ in range(T):
    N=int(input())
    List = list(map(int,input().split()))
    DP=[[float('inf') for _ in range(N)] for _ in range(N)]
    ANS=[[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N): # step
        for j in range(N-i):
            if i==0:
                DP[j][j]=List[j]
                ANS[j][j]=0
            elif i==1: #step 1 처리
                DP[j][j+i]=List[j]+List[j+i]
                ANS[j][j+i]=List[j]+List[j+i]
            else:
                for k in range(j,j+i): #해당 index를 채우기 위해 여러 step들에서 끌어오기
                    DP[j][j+i]=min(DP[j][j+i],DP[j][k]+DP[k+1][j+i])
                    ANS[j][j+i]=min(ANS[j][j+i],DP[j][k]+DP[k+1][i+j]+ANS[j][k]+ANS[k+1][i+j])
    print(ANS[0][N-1])