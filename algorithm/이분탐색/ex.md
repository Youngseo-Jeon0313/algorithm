**1300**   
"경계선"을 토대로 코드 실수하지 말자!   
```
while start <= end:
    mid = (start+end) // 2
    num  = 0
    for i in range(1, N+1):
        num += min(mid//i, N)
    if num >=K: #여기 주의 !!!
        end = mid-1
    else:
        ans = mid
        start = mid+1
print(ans)
```

**PG 입국심사**   
심사를 기다리는 사람 수 n, 심사관 times   
n=6, times =[7,10] -> 28분   
비교조건은??   
Σmid//times[i] = 25//7 + 25//10 = 5 < n --> n보다 작으면 오른쪽으로 간다.   
                                            n보다 크면 왼쪽으로 간다.   
until start <= end    

# 나무자르기 -> 적어도 M 만큼의 나무 주의!!
```
N, M = map(int,input().split())
trees = list(map(int,input().split()))
# 적어도 M 만큼의 나무
start, end = 1, max(trees)
## 이분 탐색
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in trees:
        if i > mid:
            sum += i - mid
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)

'''
5 20
4 42 40 26 47
36
'''
```