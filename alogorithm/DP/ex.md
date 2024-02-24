**BOJ 2662 기업투자**

4만원 쓸 거고  기업은 2개   
4             2   

형태   

| 요금  | A  | B  | C  |
|-----|----|----|----|
| 1만원 | 5  | 1  | 4  |
| 2만원 | 6  | 5  | 3  |
| 3만원 | 7  | 9  | 4  |  
| 4만원 | 10 | 15 | 12 |  

이 때 DP[2만원][C] = A,B 포함 C까지 포함시켰을 때 2만원으로 가지는 가장 큰 이득   
즉, DP[4만원][C] = DP A,B 포함 2만원/또는 3만원까지 쓴 것에 C 2만원/1만원 쓴 것을 더해서 나온 값..

```
import sys
input=sys.stdin.readline


N,M=map(int,input().split())#투자금 얼마?? / 기업개수

invest=[[0 for _ in range(M)] for _ in range(N+1)] # 입력값 데이터 표현
for _ in range(N):
    L=list(map(int,input().split()))
    for i in range(1,M+1):
        invest[L[0]][i-1]=L[i]

#DP[n만원을 투자했을 때][m까지의 기업까지 고려했을 때의] = 최대이익
DP=[[0 for _ in range(M)] for _ in range(N+1)]
path=[['' for _ in range(M)] for _ in range(N+1)]

#init - 기업 1의 투자금 별 해당하는 만족도
for j in range(N+1):
    DP[j][0]=invest[j][0]

for i in range(1,N+1):
    path[i][0]=str(i)+str(' ')

for j in range(M):
    path[0][j]=str(0)+str(' ')

for i in range(1,N+1): #기업 2부터 투자금별 만족도 갱신
    for k in range(i+1): 
        for j in range(1,M): #기업 2부터 쭉쭉
            if DP[k][j-1]+invest[i-k][j]>DP[i][j]:
                DP[i][j]=DP[k][j-1]+invest[i-k][j]
                path[i][j]=path[k][j-1]+str(i-k)+str(' ')


# print("DP")
# print(DP)
# print("path")
# print(path)

'''
[[0, 0, 0, 0], [0, 5, 5, 5], [0, 6, 6, 7], [0, 7, 10, 11], [0, 8, 
15, 16]]



4 1
1 5
2 6 
3 7
4 10
10
4
'''

'''
print(DP)
print(path)

[[0, 0], [5, 5], [6, 6], [7, 10], [10, 15]]
[['0 ', '0 '], ['1 ', '1 0 '], ['2 ', '1 1 '], ['3 ', '1 2 '], ['4 ', '0 4 ']]
'''




print(DP[-1][-1])
print(path[-1][-1])
```

**BOJ 1309**
2차원에서 왼쪽 없을 때 / 위쪽 없을 때 ... 로 경우를 나누어 계산하려 했으나 ?? 물리는 경우가 생기므로   
2로 준 것 !   
한 행을 기준으로 모양이 xx xo ox 세 개가 나오고 그거에 따라 아래에 나오는 유형이 다르다.   
백트래킹(NQueens)과 유형 다름 !   
