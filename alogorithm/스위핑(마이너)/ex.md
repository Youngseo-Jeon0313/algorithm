**BOJ 2170**
```
import sys
input=sys.stdin.readline


N=int(input())
List=[]

for _ in range(N):
    x,y=map(int,input().split())
    List.append([x,y])

List.sort()
result=0; l=List[0][0]; r=List[0][1]
#[l,r]: 현재 합치고 있는 구간
for i in range(N):
    #새로운 구간 도입
    if r<List[i][0]:
        #지금까지의 것 더한다.
        result+=r-l;
        #초기화
        l=List[i][0]; r=List[i][1]
    else: r=max(r,List[i][1])

result+=r-l;
print(result)
```