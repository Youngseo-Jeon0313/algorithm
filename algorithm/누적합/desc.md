### 주의(실수) - index 오류

**꼭 prefix_sum 의 맨 앞 값은 0으로 두기!**

[0, 1번째 값, 1번째 + 2번째 값, ...]   
이 때 i~i+X 만큼을 구할 때 prefix_sum[i+X] 에서 i = 0부터 !   

만약 두 개의 누적합을 이용해 
앞에서부터 + 뒤에서부터 로 파악하고 싶을 때에는
'앞이 없을 때', '뒤가 없을 때' 까지 생각해야 함 -> 이 때는 차라리 투포인터가 나을 수도 있다.

누적합은 리스트로 나타내보다가 규칙을 발견하게 될 수 있다 !   
차트?   
그림   
연속적 ??   
O O ..   
V O ..   
X V ..   
X X ..   
X X   

또는 수식을 정리하다가 발견할 수도 있다. 예를 들어 시그마(Σ) 형태가 나오거나 ...  

### 누적합 역행 로직
|   |      |   |
|---|------|---|
| ㅇ |      |   |
|   |      |   |
|   |      | ㅇ |
만약 (r1, c1) 에서부터 (r2, c2) 까지의 누적합을 역행한다고 하자.   
2 2 2 2 2 0 0   
2 2 2 2 2 0 0   
0 0 0 0 0 0 0   
0 0 0 0 0 0 0   
을 나타내고 싶다면 아래처럼 나타낸 후 누적합을 실행하면 됨!   
2 0 0 0 0 -2 0   
0 0 0 0 0 0 0   
-2 0 0 0 0 +2 0   
0 0 0 0 0 0 0    

```python
def prefix_sum(n,m):
    prefixSum = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]
    return prefixSum

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
prefixSum = prefix_sum(n,m)
i,j,x,y = map(int,input().split()) 

# (i,j)칸에서 (x,y)칸까지 포함한 부분합
partSum = prefixSum[x][y] - prefixSum[i-1][y] - prefixSum[x][j-1] + prefixSum[i-1][j-1]
print(partSum)

```